<template>
  <div>
    <v-btn
      fab
      bottom
      right
      color="pink"
      dark
      fixed
      :disabled="loading"
      @click.stop="openAddForm"
    >
      <v-icon>add</v-icon>
    </v-btn>

    <v-data-table
      :headers="headers"
      :items="customers"
      :total-items="total"
      :pagination.sync="pagination"
      :loading="loading"
      no-data-text="No customers"
      no-results-text="No customers found"
      class="elevation-1"
    >
      <template slot="items" slot-scope="{ item }">
        <td>{{ item.first_name }}</td>
        <td>{{ item.last_name }}</td>
        <td class="text-xs-right">{{ item.date_of_birth }}</td>
        <td>
          <ul v-if="item.emails && item.emails.length">
            <li v-for="{ email, id } in item.emails" :key="id">
              {{ email }}
            </li>
          </ul>
        </td>
        <td>
          <ul v-if="item.phone_numbers && item.phone_numbers.length">
            <li v-for="{ phone_number, id } in item.phone_numbers" :key="id">
              {{ phone_number }}
            </li>
          </ul>
        </td>
        <td>
          <ul v-if="item.addresses && item.addresses.length">
            <li v-for="address in item.addresses" :key="address.id">
              {{ formatAddress(address) }}
            </li>
          </ul>
          <i v-else>No address</i>
        </td>
        <td>
          <v-btn small color="primary" @click="openViewDialog(item)">View</v-btn>
          <v-btn small color="warning" @click="openEditForm(item)">Edit</v-btn>
          <v-btn small color="error" @click="deleteCustomer(item.id)">Delete</v-btn>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="viewForm" width="800px" persistent>
      <customer-view />
    </v-dialog>

    <v-dialog v-model="editForm" width="1000px" scrollable persistent>
      <customer-form />
    </v-dialog>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import utils from '@/mixins/utils'

export default {
  mixins: [utils],
  data() {
    return {
      headers: [
        {
          text: 'First Name',
          align: 'left',
          value: 'first_name',
          sortable: false
        },
        {
          text: 'Last Name',
          align: 'left',
          value: 'last_name',
          sortable: false
        },
        {
          text: 'Date of Birth',
          value: 'date_of_birth',
          sortable: false
        },
        {
          text: 'Email(s)',
          align: 'left',
          value: 'email',
          sortable: false
        },
        {
          text: 'Phone Number(s)',
          align: 'left',
          value: 'phone_number',
          sortable: false
        },
        {
          text: 'Address(es)',
          align: 'left',
          value: 'address',
          sortable: false
        },
        {
          text: 'Actions',
          align: 'left',
          value: 'actions',
          sortable: false
        }
      ]
    }
  },

  computed: {
    pagination: {
      get: function() {
        return this.$store.state.pagination
      },
      set: function(payload) {
        this.paginate(payload)
      }
    },
    ...mapGetters(['customers', 'total', 'loading', 'viewForm', 'editForm'])
  },

  methods: {
    openAddForm() {
      this.setCustomerDefault()
      this.setEditting(false)
      this.setEditForm(true)
    },
    openEditForm(customer) {
      this.setCustomer(customer)
      this.setEditting(true)
      this.setEditForm(true)
    },
    openViewDialog(customer) {
      this.setCustomer(customer)
      this.setViewForm(true)
    },
    deleteCustomer(id) {
      if (confirm('Are you sure to remove this customer?')) {
        this.$store.dispatch('deleteCustomer', id)
      }
    },
    ...mapActions([
      'getCustomers',
      'paginate',
      'setCustomerDefault',
      'setCustomer',
      'setViewForm',
      'setEditForm',
      'setEditting'
    ])
  }
}
</script>

<style lang="scss" scoped>

</style>
