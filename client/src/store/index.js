import Vue from 'vue'
import Vuex from 'vuex'
import cloneDeep from 'lodash/cloneDeep'
import * as CountryList from 'country-list'

import * as api from '@/api'

Vue.use(Vuex)

const state = {
  customers: [],
  status: {
    loading: false,
    success: false,
    error: false
  },
  customer: {
    emails: [],
    phone_numbers: [],
    addresses: []
  },
  countries: CountryList().getData(),
  viewForm: false,
  editForm: false,
  editting: false,
  pagination: {
    sortBy: '',
    page: 1,
    rowsPerPage: 5,
    descending: false
  },
  total: 0
}

const getters = {
  customers(state) {
    return state.customers
  },
  total(state) {
    return state.total
  },
  customerModel(state) {
    return state.customer
  },
  countries(state) {
    return state.countries
  },
  loading(state) {
    return state.status.loading
  },
  viewForm(state) {
    return state.viewForm
  },
  editForm(state) {
    return state.editForm
  },
  editting(state) {
    return state.editting
  },
  pagination(state) {
    return state.pagination
  }
}

const mutations = {
  SET_TOTAL(state, payload) {
    state.total = payload
  },
  SET_CUSTOMERS(state, payload) {
    state.customers = payload
  },
  SET_CUSTOMER(state, payload) {
    state.customer = payload
  },
  LOADING(state) {
    state.status = {
      loading: true,
      success: false,
      error: false
    }
  },
  SUCCESS(state) {
    state.status = {
      loading: false,
      success: true,
      error: false
    }
  },
  ERROR(state, payload) {
    state.status = {
      loading: false,
      success: false,
      error: payload
    }
  },
  CLEAR_ERROR(state) {
    state.status = {
      loading: false,
      success: false,
      error: false
    }
  },
  TOGGLE_VIEWFORM(state, payload) {
    state.viewForm = payload
  },
  TOGGLE_EDITFORM(state, payload) {
    state.editForm = payload
  },
  TOGGLE_EDITTING(state, payload) {
    state.editting = payload
  },
  ADD_CUSTOMER_EMAIL(state, payload) {
    state.customer.emails.push(payload)
  },
  REMOVE_CUSTOMER_EMAIL(state, payload) {
    state.customer.emails.splice(payload, 1)
  },
  ADD_CUSTOMER_PHONE_NUMBER(state, payload) {
    state.customer.phone_numbers.push(payload)
  },
  REMOVE_CUSTOMER_PHONE_NUMBER(state, payload) {
    state.customer.phone_numbers.splice(payload, 1)
  },
  ADD_CUSTOMER_ADDRESS(state, payload) {
    state.customer.addresses.push(payload)
  },
  REMOVE_CUSTOMER_ADDRESS(state, payload) {
    state.customer.addresses.splice(payload, 1)
  },
  SET_CUSTOMER_DEFAULT(state) {
    state.customer = {
      emails: [{}],
      phone_numbers: [{}],
      addresses: []
    }
  },
  PAGINATE(state, payload) {
    state.pagination = payload
  }
}

const actions = {
  paginate({ commit, dispatch }, payload) {
    commit('PAGINATE', payload)
    dispatch('getCustomers')
  },
  getCustomers({ commit, getters: { pagination } }) {
    commit('LOADING')

    api
      .getCustomers({
        page: pagination.page,
        page_size: pagination.rowsPerPage
      })
      .then(res => {
        commit('SET_CUSTOMERS', res.data.results)
        commit('SET_TOTAL', res.data.count)
        commit('SUCCESS')
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },
  setCustomer({ commit }, payload) {
    commit('SET_CUSTOMER', cloneDeep(payload))
  },
  setCustomerDefault({ commit }) {
    commit('SET_CUSTOMER_DEFAULT')
  },
  addCustomer({ commit, dispatch }, payload) {
    commit('LOADING')

    api
      .addCustomer(payload)
      .then(res => {
        commit('SUCCESS')

        commit('TOGGLE_EDITFORM', false)
        commit('SET_CUSTOMER', res.data)
        commit('TOGGLE_VIEWFORM', true)

        dispatch('getCustomers')
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },
  editCustomer({ commit, dispatch }, payload) {
    commit('LOADING')

    api
      .editCustomer(payload)
      .then(res => {
        commit('SUCCESS')

        commit('TOGGLE_EDITFORM', false)
        commit('SET_CUSTOMER', res.data)
        commit('TOGGLE_VIEWFORM', true)

        dispatch('getCustomers')
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },
  deleteCustomer({ commit, dispatch }, payload) {
    commit('LOADING')

    api
      .deleteCustomer(payload)
      .then(res => {
        if (res.status === 204) {
          commit('SUCCESS')

          dispatch('getCustomers')
        } else {
          commit('ERROR', res)
        }
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },
  clearError({ commit }) {
    commit('CLEAR_ERROR')
  },
  setViewForm({ commit }, payload) {
    commit('TOGGLE_VIEWFORM', payload)
  },
  setEditForm({ commit }, payload) {
    commit('TOGGLE_EDITFORM', payload)
  },
  setEditting({ commit }, payload) {
    commit('TOGGLE_EDITTING', payload)
  },
  addCustomerEmail(context, payload) {
    context.commit('ADD_CUSTOMER_EMAIL', payload)
  },
  removeCustomerEmail(context, payload) {
    context.commit('REMOVE_CUSTOMER_EMAIL', payload)
  },
  addCustomerPhoneNumber(context, payload) {
    context.commit('ADD_CUSTOMER_PHONE_NUMBER', payload)
  },
  removeCustomerPhoneNumber(context, payload) {
    context.commit('REMOVE_CUSTOMER_PHONE_NUMBER', payload)
  },
  addCustomerAddress(context, payload) {
    context.commit('ADD_CUSTOMER_ADDRESS', payload)
  },
  removeCustomerAddress(context, payload) {
    context.commit('REMOVE_CUSTOMER_ADDRESS', payload)
  }
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
