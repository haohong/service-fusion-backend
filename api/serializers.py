from collections import Counter
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Person, Address, Email, PhoneNumber


def has_duplicate(l):
    return next((True for k, v in Counter(l).items() if v > 1), False)


class CustomListSerializer(serializers.ListSerializer):
    """Custom ListSerializer"""

    def create(self, validated_data):
        child_class = self.child.Meta.model

        children = [child_class(**child_data) for child_data in validated_data]
        return child_class.objects.bulk_create(children)

    def update(self, instance, validated_data):
        # Maps for id->instance.
        child_mapping = {child.id: child for child in instance}

        # Perform creations and updates.
        ret = []
        updated_child_ids = []
        for child_data in validated_data:
            child_id = child_data.pop('id', None)
            child = child_mapping.get(child_id, None)

            if child is None:
                ret.append(self.child.create(child_data))
            else:
                updated_child_ids.append(child_id)
                ret.append(self.child.update(child, child_data))

        # Perform deletions.
        for child_id, child in child_mapping.items():
            if child_id not in updated_child_ids:
                child.delete()

        return ret


class AddressSerializer(serializers.ModelSerializer):
    """Serializer to map the Address model instance into JSON format."""
    id = serializers.IntegerField(required=False)

    class Meta:
        """Meta class to map serializer's fields with model fields."""

        model = Address
        fields = ('id', 'address1', 'address2', 'city',
                  'state', 'country', 'zip_code',)
        list_serializer_class = CustomListSerializer


class EmailSerializer(serializers.ModelSerializer):
    """Serializer to map the Email model instance into JSON format."""

    id = serializers.IntegerField(required=False)

    class Meta:
        """Meta class to map serializer's fields with model fields."""

        model = Email
        fields = ('id', 'email',)
        list_serializer_class = CustomListSerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    """Serializer to map the PhoneNumber model instance into JSON format."""

    id = serializers.IntegerField(required=False)
    phone_number = PhoneNumberField()

    class Meta:
        """Meta class to map serializer's fields with model fields."""

        model = PhoneNumber
        fields = ('id', 'phone_number',)
        list_serializer_class = CustomListSerializer


class PersonSerializer(serializers.ModelSerializer):
    """Serializer to map the Person model instance into JSON format."""

    addresses = AddressSerializer(many=True, allow_empty=True, required=False)
    emails = EmailSerializer(many=True, allow_empty=False, required=True)
    phone_numbers = PhoneNumberSerializer(
        many=True, allow_empty=False, required=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Person
        fields = ('id', 'first_name', 'last_name', 'date_of_birth',
                  'addresses', 'emails', 'phone_numbers')

    def validate_addresses(self, value):
        """
        Add owner_id field to addresses data
        """
        if self.instance:
            for address_data in value:
                address_data['owner_id'] = self.instance.id

        return value

    def validate_emails(self, value):
        """
        Check if there are duplicate emails
        Check if emails already exist in db
        Add owner_id field to emails data
        """
        emails = [email_data['email'] for email_data in value]
        if has_duplicate(emails):
            raise serializers.ValidationError("Duplicate emails in payload.")

        queryset = Email.objects.filter(email__in=emails)
        if self.instance:
            existing_email_ids = [
                email.id for email in self.instance.emails.all()]
            queryset = queryset.exclude(id__in=existing_email_ids)

        if queryset:
            errors = ["{} already exists.".format(e.email) for e in queryset]
            raise serializers.ValidationError(errors)

        if self.instance:
            for email_data in value:
                email_data['owner_id'] = self.instance.id

        return value

    def validate_phone_numbers(self, value):
        """
        Check if there are duplicate phone_numbers
        Check if phone_numbers already exist in db
        Add owner_id field to phone_numbers data
        """
        phone_numbers = [phone_number_data['phone_number']
                         for phone_number_data in value]
        if has_duplicate(phone_numbers):
            raise serializers.ValidationError(
                "Duplicate phone_numbers in payload.")

        queryset = PhoneNumber.objects.filter(phone_number__in=phone_numbers)
        if self.instance:
            existing_phone_number_ids = [
                phone_number.id for phone_number in self.instance.phone_numbers.all()]
            queryset = queryset.exclude(id__in=existing_phone_number_ids)

        if queryset:
            errors = ["{} already exists.".format(
                e.phone_number) for e in queryset]
            raise serializers.ValidationError(errors)

        if self.instance:
            for phone_number_data in value:
                phone_number_data['owner_id'] = self.instance.id

        return value

    def create(self, validated_data):
        """Create"""
        self.instance = Person.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'])

        addresses_data = validated_data.pop('addresses', None)
        if addresses_data is not None:
            self.fields['addresses'].create(
                self.validate_addresses(addresses_data))

        emails_data = validated_data.pop('emails', None)
        if emails_data is not None:
            self.fields['emails'].create(
                self.validate_emails(emails_data))

        phone_numbers_data = validated_data.pop('phone_numbers', None)
        if phone_numbers_data is not None:
            self.fields['phone_numbers'].create(
                self.validate_phone_numbers(phone_numbers_data))

        return self.instance

    def update(self, instance, validated_data):
        """Update"""

        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.date_of_birth = validated_data.get(
            'date_of_birth', instance.date_of_birth)
        instance.save()

        addresses_data = validated_data.pop('addresses', None)
        if addresses_data is not None:
            self.fields['addresses'].update(
                instance.addresses.all(), addresses_data)

        emails_data = validated_data.pop('emails', None)
        if emails_data is not None:
            self.fields['emails'].update(
                instance.emails.all(), emails_data)

        phone_numbers_data = validated_data.pop('phone_numbers', None)
        if phone_numbers_data is not None:
            self.fields['phone_numbers'].update(
                instance.phone_numbers.all(), phone_numbers_data)

        return instance
