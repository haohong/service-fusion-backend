// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'

import store from './store'

import App from './App'
import CustomerList from './components/CustomerList'
import CustomerView from './components/CustomerView'
import CustomerForm from './components/CustomerForm'
import router from './router'

Vue.use(Vuetify)

Vue.component('CustomerList', CustomerList)
Vue.component('CustomerView', CustomerView)
Vue.component('CustomerForm', CustomerForm)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})
