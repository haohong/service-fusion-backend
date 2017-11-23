<template>
  <v-card>
    <v-card-title
      class="grey lighten-4 py-4 title"
    >
      Customer Details
    </v-card-title>

    <v-container grid-list-sm class="pa-4">

      <v-layout row>
        <v-flex xs3>
          <v-subheader>Name</v-subheader>
        </v-flex>
        <v-flex xs9 class="ml-3 mt-2">
          <v-layout align-center>
            <v-avatar size="40px" class="mr-3">
              <v-icon medium>account_circle</v-icon>
            </v-avatar>
            <span class="subheading">{{ `${customer.first_name} ${customer.last_name}` }}</span>
          </v-layout>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs3>
          <v-subheader>Date of Birth</v-subheader>
        </v-flex>
        <v-flex xs9 class="ml-3 mt-2">
          <v-layout align-center>
            <v-avatar size="40px" class="mr-3">
              <v-icon medium>perm_contact_calendar</v-icon>
            </v-avatar>
            <span class="subheading">{{ `${customer.date_of_birth}` }}</span>
          </v-layout>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs3>
          <v-subheader>Email(s)</v-subheader>
        </v-flex>
        <v-flex xs9 class="ml-3 mt-2">
          <div v-if="customer.emails && customer.emails.length">
            <v-layout v-for="{email, id} in customer.emails" align-center :key="id">
              <v-avatar size="40px" class="mr-3">
                <v-icon medium>email</v-icon>
              </v-avatar>
              <span class="subheading">{{ `${email}` }}</span>
            </v-layout>
          </div>
          <div v-else class="ma-1">
            <i class="subheading">No Email</i>
          </div>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs3>
          <v-subheader>Phone Number(s)</v-subheader>
        </v-flex>
        <v-flex xs9 class="ml-3 mt-2">
          <div v-if="customer.phone_numbers && customer.phone_numbers.length">
            <v-layout v-for="{phone_number, id} in customer.phone_numbers" align-center :key="id">
              <v-avatar size="40px" class="mr-3">
                <v-icon medium>phone</v-icon>
              </v-avatar>
              <span class="subheading">{{ `${phone_number}` }}</span>
            </v-layout>
          </div>
          <div v-else class="ma-1">
            <i class="subheading">No Phone Number</i>
          </div>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs3>
          <v-subheader>Address(es)</v-subheader>
        </v-flex>
        <v-flex xs9 class="ml-3 mt-2">
          <div v-if="customer.addresses && customer.addresses.length">
            <v-layout row
              v-for="address in customer.addresses"
              align-center
              :key="address.id"
            >
              <v-avatar size="40px" class="mr-3">
                <v-icon medium>room</v-icon>
              </v-avatar>
              <span class="subheading">{{ formatAddress(address) }}</span>
            </v-layout>
          </div>
          <div v-else class="ma-1">
            <i class="subheading">No Address</i>
          </div>
        </v-flex>
      </v-layout>

    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click.native="close">Close</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import utils from '@/mixins/utils'

export default {
  mixins: [utils],
  computed: {
    ...mapGetters({
      customer: 'customerModel'
    })
  },
  methods: {
    close() {
      this.setViewForm(false)
    },
    ...mapActions(['setViewForm'])
  }
}
</script>
