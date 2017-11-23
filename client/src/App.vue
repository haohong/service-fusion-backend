<template>
  <v-app id="inspire">
    <v-toolbar
      color="blue darken-3"
      dark
      app
      clipped-left
      fixed
    >
      <v-toolbar-title :style="$vuetify.breakpoint.smAndUp ? 'width: 400px; min-width: 250px' : 'min-width: 72px'" class="ml-0 pl-3">
        <span class="hidden-xs-only">ServiceFusion Customers</span>
      </v-toolbar-title>
      <v-text-field
        light
        solo
        prepend-icon="search"
        placeholder="Search"
        style="max-width: 500px; min-width: 128px"
      ></v-text-field>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <customer-list />
      </v-container>
    </v-content>

    <v-snackbar :timeout="2000" color="success" v-model="success">
      Request done successfully!
    </v-snackbar>

    <v-snackbar :timeout="5000" color="error" v-model="error">
      <ul>
        <li v-for="(error, index) in errorArr" :key="index">
          {{ error }}
        </li>
      </ul>
    </v-snackbar>

  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
import * as _ from 'lodash'

export default {
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
        return !!this.$store.state.status.error
      },
      set: function(value) {
        this.clearError()
      }
    },
    errorArr: function() {
      const errorMap = this.$store.state.status.error

      return _.reduce(
        errorMap,
        (result, val, key) => {
          const field = _.capitalize(key)
          const errors = _.flatMap(
            val,
            error => (_.isObject(error) ? _.values(error) : error)
          )

          result = result.concat(errors.map(error => `${field}: ${error}`))

          return result
        },
        []
      )
    }
  },
  methods: {
    ...mapActions(['clearError'])
  }
}
</script>
