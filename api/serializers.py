from rest_framework import serializers

from .models import Person, Address


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
        existing_child_ids = []
        for child_data in validated_data:
            child_id = child_data.pop('id', None)
            child = child_mapping.get(child_id, None)

            if child is None:
                ret.append(self.child.create(child_data))
            else:
                existing_child_ids.append(child_id)
                ret.append(self.child.update(child, child_data))

        # Perform deletions.
        for child_id, child in child_mapping.items():
            if child_id not in existing_child_ids:
                child.delete()

        return ret


class AddressSerializer(serializers.ModelSerializer):
    """Serializer to map the address model instance into JSON format."""

    id = serializers.IntegerField(required=False)  # Making id writable

    class Meta:
        """Meta class to map serializer's fields with model fields."""

        model = Address
        fields = ('id', 'address1', 'address2', 'city',
                  'state', 'country', 'zip_code')
        list_serializer_class = CustomListSerializer


class PersonSerializer(serializers.ModelSerializer):
    """Serializer to map the person model instance into JSON format."""

    addresses = AddressSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Person
        fields = ('id', 'first_name', 'last_name',
                  'date_of_birth', 'addresses')

    def validate_addresses(self, value):
        """
        Add owner_id fields to addresses data
        """
        if self.instance:
            for address_data in value:
                address_data['owner_id'] = self.instance.id

        return value

    def create(self, validated_data):
        """Create"""
        addresses_data = validated_data.pop('addresses', None)
        self.instance = Person.objects.create(**validated_data)

        if addresses_data is not None:
            self.fields['addresses'].create(
                self.validate_addresses(addresses_data))

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

        return instance
