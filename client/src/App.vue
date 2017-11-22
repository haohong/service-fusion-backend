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

    <v-btn
      fab
      bottom
      right
      color="pink"
      dark
      fixed
      @click.stop="dialog = !dialog"
    >
      <v-icon>add</v-icon>
    </v-btn>

    <v-dialog v-model="dialog" width="1000px" persistent>
      <customer-form :customer="customer" @cancel="cancelAdd"/>
    </v-dialog>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    customer: {}
  }),
  methods: {
    addCustomer() {
      this.dialog = true
    },
    cancelAdd() {
      this.dialog = false
    }
  }
}
</script>
