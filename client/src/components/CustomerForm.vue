<template>
  <v-card>
    <v-form @submit.prevent="submit">
      <v-card-title
        class="grey lighten-4 py-4 title"
      >
        {{ editting ? 'Edit ' : 'Add ' }} Customer
      </v-card-title>

      <v-card-text style="height: 600px">

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
                  v-model="customerModel.first_name"
                  prepend-icon="account_circle"
                  required
                ></v-text-field>
              </v-flex>
              <v-flex xs5>
                <v-text-field
                  type="text"
                  name="last_name"
                  label="Last Name"
                  v-model="customerModel.last_name"
                  required
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
              v-model="customerModel.date_of_birth"
              prepend-icon="perm_contact_calendar"
            ></v-text-field>
          </v-flex>
        </v-layout>

        <v-layout row>
          <v-flex xs2>
            <v-subheader>Email</v-subheader>
          </v-flex>
          <v-flex xs10>
            <v-layout
              v-for="(item, index) in customerModel.emails"
              :key="index"
              align-center
            >
              <v-flex>
                <v-text-field
                  type="email"
                  name="email"
                  label="Email"
                  v-model="item.email"
                  prepend-icon="email"
                ></v-text-field>
              </v-flex>

              <div style="width: 60px" class="text-xs-right">
                <v-btn color="error" fab dark small @click="removeEmail(index)">
                  <v-icon dark>remove</v-icon>
                </v-btn>
              </div>
            </v-layout>

            <v-btn color="primary" fab small dark @click="addEmail">
              <v-icon>add</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

        <v-layout row>
          <v-flex xs2>
            <v-subheader>Phone Number</v-subheader>
          </v-flex>
          <v-flex xs10>
            <v-layout
              v-for="(item, index) in customerModel.phone_numbers"
              :key="index"
              align-center
            >
              <v-flex>
                <v-text-field
                  type="text"
                  name="phone_number"
                  label="Phone Number"
                  v-model="item.phone_number"
                  prepend-icon="phone"
                ></v-text-field>
              </v-flex>

              <div style="width: 60px" class="text-xs-right">
                <v-btn color="error" fab dark small @click="removePhoneNumber(index)">
                  <v-icon dark>remove</v-icon>
                </v-btn>
              </div>
            </v-layout>

            <v-btn color="primary" fab small dark @click="addPhoneNumber">
              <v-icon>add</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

        <v-layout row>
          <v-flex xs2>
            <v-subheader>Address</v-subheader>
          </v-flex>
          <v-flex xs10>
            <v-layout
              v-for="(item, index) in customerModel.addresses"
              :key="index"
              align-center
            >
              <v-flex>
                <v-layout row wrap>
                  <v-flex xs7>
                    <v-select
                      :items="countries"
                      item-value="code"
                      item-text="name"
                      label="Country"
                      v-model="item.country"
                      prepend-icon="room"
                    ></v-select>
                  </v-flex>

                  <v-flex xs5>
                    <v-text-field
                      type="text"
                      name="state"
                      label="State"
                      v-model="item.state"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs8>
                    <v-text-field
                      type="text"
                      name="city"
                      label="City"
                      v-model="item.city"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs4>
                    <v-text-field
                      type="text"
                      name="zip_code"
                      label="Zip Code"
                      v-model="item.zip_code"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs6>
                    <v-text-field
                      type="text"
                      name="address1"
                      label="Address1"
                      v-model="item.address1"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs6>
                    <v-text-field
                      type="text"
                      name="address2"
                      label="Address2"
                      v-model="item.address2"
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>

              <div style="width: 60px" class="text-xs-right">
                <v-btn color="error" fab dark small @click="removeAddress(index)">
                  <v-icon dark>remove</v-icon>
                </v-btn>
              </div>
            </v-layout>

            <v-btn color="primary" fab small dark @click="addAddress">
              <v-icon>add</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn color="primary" type="submit">Save</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  data: () => ({
    dialog: false
  }),
  computed: {
    ...mapGetters([
      'editForm',
      'customerModel',
      'countries',
      'editting',
      'loading'
    ])
  },
  methods: {
    submit(e) {
      console.log('submit')
    },
    cancel() {
      this.setEditForm(false)
    },
    addEmail() {
      this.addCustomerEmail({})
    },
    removeEmail(index) {
      this.removeCustomerEmail(index)
    },
    addPhoneNumber() {
      this.addCustomerPhoneNumber({})
    },
    removePhoneNumber(index) {
      this.removeCustomerPhoneNumber(index)
    },
    addAddress() {
      this.addCustomerAddress({})
    },
    removeAddress(index) {
      this.removeCustomerAddress(index)
    },
    ...mapActions([
      'setEditForm',
      'addCustomerEmail',
      'removeCustomerEmail',
      'addCustomerPhoneNumber',
      'removeCustomerPhoneNumber',
      'addCustomerAddress',
      'removeCustomerAddress'
    ])
  }
}
</script>
