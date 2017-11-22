<template>
  <div>
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
          <v-btn small color="error" @click="deleteCustomer(item)">Delete</v-btn>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="viewForm" width="800px" persistent>
      <customer-view :customer="selectedCustomer" @close="closeViewDialog"/>
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
      ],
      selectedCustomer: {}
    }
  },

  computed: {
    success: {
      get: function() {
        return this.$store.state.status.success
      },
      set: function(value) {
        this.clearError()
      }
    },
    error: {
      get: function() {
        return this.$store.state.status.error
      },
      set: function(value) {
        this.clearError()
      }
    },
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

  mounted() {
    this.getCustomers()
  },

  methods: {
    openViewDialog(customer) {
      this.selectedCustomer = customer
      this.setViewForm(true)
    },
    closeViewDialog() {
      this.setViewForm(false)
    },
    deleteCustomer(customer) {
      console.log('delete', customer)
    },
    ...mapActions(['getCustomers', 'clearError', 'paginate', 'setViewForm'])
  }
}
</script>

<style lang="scss" scoped>

</style>
