<template>
  <div>
    <v-data-table
        :headers="headers"
        :items="customers"
        no-data-text="No customers"
        no-results-text="No customers found"
        class="elevation-1"
      >
      <template slot="items" slot-scope="{ item, index }">
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
          <v-btn small color="primary" @click="viewCustomer(index)">View</v-btn>
          <v-btn small color="error" @click="deleteCustomer(index)">Delete</v-btn>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" width="800px" persistent>
      <customer-view :customer="selectedCustomer" @close="closeCustomer"/>
    </v-dialog>
  </div>
</template>

<script>
import utils from '@/mixins/utils'

export default {
  mixins: [utils],
  data() {
    return {
      headers: [
        {
          text: 'First Name',
          align: 'left',
          value: 'first_name'
        },
        {
          text: 'Last Name',
          align: 'left',
          value: 'last_name'
        },
        {
          text: 'Date of Birth',
          value: 'date_of_birth'
        },
        {
          text: 'Email(s)',
          align: 'left',
          value: 'email'
        },
        {
          text: 'Phone Number(s)',
          align: 'left',
          value: 'phone_number'
        },
        {
          text: 'Address(es)',
          align: 'left',
          value: 'address'
        },
        {
          text: 'Actions',
          align: 'left',
          value: 'actions'
        }
      ],
      customers: [
        {
          first_name: 'Haohong',
          last_name: 'Xu',
          date_of_birth: '1990-02-17',
          addresses: [
            {
              id: 2,
              address1: '123, Abc',
              address2: '',
              city: 'Los Angeles',
              state: 'California',
              country: 'US',
              zip_code: '23432'
            },
            {
              id: 3,
              address1: '123, Abc',
              address2: '',
              city: 'Los Angeles',
              state: 'California',
              country: 'US',
              zip_code: '23432'
            }
          ],
          emails: [
            {
              id: 15,
              email: 'haohong1234@gmail.com'
            },
            {
              id: 16,
              email: 'haohong1234@gmail.com'
            }
          ],
          phone_numbers: [
            {
              id: 4,
              phone_number: '+12345678911'
            },
            {
              id: 3,
              phone_number: '+12345678911'
            }
          ]
        }
      ],
      dialog: false,
      selectedCustomerId: null
    }
  },

  computed: {
    selectedCustomer() {
      return this.selectedCustomerId >= 0 &&
        this.selectedCustomerId < this.customers.length
        ? this.customers[this.selectedCustomerId]
        : null
    }
  },

  methods: {
    viewCustomer(index) {
      this.dialog = true
      this.selectedCustomerId = index
    },
    closeCustomer() {
      this.dialog = false
      this.selectedCustomerId = null
    },
    deleteCustomer(index) {
      console.log('delete', index)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
