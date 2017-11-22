<template>
  <v-card>
    <v-card-title
      class="grey lighten-4 py-4 title"
    >
      Create customer
    </v-card-title>

    <v-container grid-list-sm class="pa-4">

      <v-layout row>
        <v-flex xs2>
          <v-subheader>Name</v-subheader>
        </v-flex>
        <v-flex xs10>
          <v-layout>
            <v-flex xs7>
              <v-text-field
                type="text"
                name="first_name"
                label="First Name"
                v-model="customer.first_name"
                prepend-icon="account_circle"
              ></v-text-field>
            </v-flex>
            <v-flex xs5>
              <v-text-field
                type="text"
                name="last_name"
                label="Last Name"
                v-model="customer.last_name"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs2>
          <v-subheader>Date of Birth</v-subheader>
        </v-flex>
        <v-flex xs10>
          <v-text-field
            type="date"
            name="date_of_birth"
            label="Date of Birth"
            v-model="customer.date_of_birth"
            prepend-icon="perm_contact_calendar"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs2>
          <v-subheader>Email</v-subheader>
        </v-flex>
        <v-flex xs10>
          <v-text-field
            type="email"
            name="email"
            label="Email"
            prepend-icon="email"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs2>
          <v-subheader>Phone Number</v-subheader>
        </v-flex>
        <v-flex xs10>
          <v-text-field
            type="text"
            name="phone_number"
            label="Phone Number"
            prepend-icon="phone"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs2>
          <v-subheader>Address</v-subheader>
        </v-flex>
        <v-flex xs10>
          <v-layout row wrap>
            <v-flex xs7>
              <v-select
                :items="countries"
                item-value="code"
                item-text="name"
                label="Country"
                single-line
                bottom
                prepend-icon="room"
              ></v-select>
            </v-flex>

            <v-flex xs5>
              <v-text-field
                type="text"
                name="state"
                label="State"
              ></v-text-field>
            </v-flex>

            <v-flex xs8>
              <v-text-field
                type="text"
                name="city"
                label="City"
              ></v-text-field>
            </v-flex>

            <v-flex xs4>
              <v-text-field
                type="text"
                name="zip_code"
                label="Zip Code"
              ></v-text-field>
            </v-flex>

            <v-flex xs6>
              <v-text-field
                type="text"
                name="address1"
                label="Address1"
              ></v-text-field>
            </v-flex>

            <v-flex xs6>
              <v-text-field
                type="text"
                name="address2"
                label="Address2"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>

    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="cancel">Cancel</v-btn>
      <v-btn color="primary" @click="submit">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import * as CountryList from 'country-list'

export default {
  created () {
    this.countries = CountryList().getData()
  },
  data: () => ({
    dialog: false
  }),
  props: {
    customer: {
      type: Object,
      default: () => ({})
    }
  },
  methods: {
    submit(e) {
      console.log('submit')
    },
    cancel() {
      this.$emit('cancel')
    }
  }
}
</script>
