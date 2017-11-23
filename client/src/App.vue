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

    <v-snackbar :timeout="3000" color="error" v-model="error">
      There was an error during request!
    </v-snackbar>

  </v-app>
</template>

<script>
import { mapActions } from 'vuex'

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
    }
  },
  methods: {
    ...mapActions(['clearError'])
  }
}
</script>
