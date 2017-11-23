<template>
  <v-card>
    <v-form
      v-model="formValid"
      ref="form"
      lazy-validation
      @submit.prevent="submit"
    >
      <v-card-title
        class="grey lighten-4 py-4 title"
      >
        {{ editting ? 'Edit ' : 'Add ' }} Customer
      </v-card-title>

      <v-card-text style="height: 600px">

        <v-progress-linear v-show="loading" height="2" :indeterminate="true"></v-progress-linear>

        <v-layout row>
          <v-flex xs2>
            <v-subheader>Name</v-subheader>
          </v-flex>
          <v-flex xs10>
            <v-layout>
              <v-flex xs7>
                <v-text-field
                  type="text"
                  label="First Name"
                  v-model="customerModel.first_name"
                  prepend-icon="account_circle"
                  :rules="[rules.required]"
                  required
                ></v-text-field>
              </v-flex>
              <v-flex xs5>
                <v-text-field
                  type="text"
                  label="Last Name"
                  v-model="customerModel.last_name"
                  :rules="[rules.required]"
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
          <v-flex xs5>
            <v-text-field
              type="date"
              label="Date of Birth"
              v-model="customerModel.date_of_birth"
              prepend-icon="perm_contact_calendar"
              :rules="[rules.required]"
              required
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
                  label="Email"
                  v-model="item.email"
                  prepend-icon="email"
                  :rules="[rules.required, rules.email]"
                  required
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
                  label="Phone Number"
                  v-model="item.phone_number"
                  prepend-icon="phone"
                  :rules="[rules.required, rules.phoneNumber]"
                  required
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
                      :rules="[rules.required]"
                      required
                    ></v-select>
                  </v-flex>

                  <v-flex xs5>
                    <v-text-field
                      type="text"
                      label="State"
                      v-model="item.state"
                      :rules="[rules.required]"
                      required
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs8>
                    <v-text-field
                      type="text"
                      label="City"
                      v-model="item.city"
                      :rules="[rules.required]"
                      required
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs4>
                    <v-text-field
                      type="text"
                      label="Zip Code"
                      v-model="item.zip_code"
                      :rules="[rules.required, rules.zipCode]"
                      required
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs6>
                    <v-text-field
                      type="text"
                      label="Address1"
                      v-model="item.address1"
                      :rules="[rules.required]"
                      required
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs6>
                    <v-text-field
                      type="text"
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
        <v-btn color="primary" type="submit" :disabled="!formValid">Save</v-btn>
      </v-card-actions>

    </v-form>

    <v-snackbar :timeout="3000" v-model="formError" top color="error" absolute>
      <ul>
        <li v-for="(formError, index) in formErrors" :key="index">
          {{ formError }}
        </li>
      </ul>
    </v-snackbar>

  </v-card>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'

import validators from '@/mixins/validators'

export default {
  mixins: [validators],
  data() {
    return {
      formValid: true,
      formErrors: []
    }
  },
  computed: {
    formError: {
      get: function() {
        return this.formErrors.length > 0
      },
      set: function(value) {
        if (!value) {
          this.formErrors = []
        }
      }
    },
    ...mapGetters(['customerModel', 'countries', 'editting', 'loading'])
  },
  watch: {
    editting: function(editting) {
      // If new form, reset the form
      if (!editting) {
        this.$refs.form.reset()
      }
    }
  },
  methods: {
    validateAtFormLevel() {
      this.formErrors = []

      if (this.customerModel.emails.length === 0) {
        this.formErrors.push('Must have at least 1 email.')
      }

      if (this.customerModel.phone_numbers.length === 0) {
        this.formErrors.push('Must have at least 1 phone number.')
      }
    },
    submit() {
      if (!this.$refs.form.validate()) {
        return
      }

      this.validateAtFormLevel()

      if (this.formError) {
        return
      }

      this.editting
        ? this.editCustomer(this.customerModel)
        : this.addCustomer(this.customerModel)
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
      'removeCustomerAddress',
      'addCustomer',
      'editCustomer'
    ])
  }
}
</script>
