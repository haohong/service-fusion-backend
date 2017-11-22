import Vue from 'vue'
import Vuex from 'vuex'

import * as api from '@/api'

Vue.use(Vuex)

const state = {
  customers: [],
  status: {
    loading: false,
    success: false,
    error: false
  },
  editForm: false,
  editting: false,
  pagination: {
    page: 1,
    page_size: 12
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
  loading(state) {
    return state.status.loading
  },
  editForm(state) {
    return state.editForm
  },
  editting(state) {
    return state.editting
  },
  pagination(state) {
    return state.pagination
  },
  page(state) {
    return state.pagination.page
  }
}

const mutations = {
  SET_TOTAL(state, payload) {
    state.total = payload
  },
  SET_CUSTOMERS(state, payload) {
    state.customers = payload
  },
  // SET_CUSTOMER(state, payload) {
  //   state.customer = payload
  // },
  // ADD_CUSTOMER(state, payload) {
  //   state.customers.unshift(payload)
  // },
  // EDIT_CUSTOMER(state, payload) {
  //   state.customers = _.unionBy([payload], state.customers, '_id')
  // },
  // DELETE_CUSTOMER(state, payload) {
  //   _.remove(state.customers, function(customer) {
  //     return customer._id === payload._id
  //   })
  // },
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
  TOGGLE_EDITFORM(state, payload) {
    state.editForm = payload
  },
  TOGGLE_EDITTING(state) {
    state.editting = !state.editting
  },
  PAGINATE(state, payload) {
    state.pagination.page = payload
  }
}

const actions = {
  getCustomers({ commit, getters }) {
    commit('LOADING')

    api
      .getCustomers(getters.pagination)
      .then(res => {
        commit('SET_CUSTOMERS', res.data.results)
        commit('SET_TOTAL', res.data.count)
        commit('SUCCESS')
      })
      .catch(e => {
        commit('ERROR', e)
      })
  }
  // editCustomer(context, payload) {
  //   context.commit('LOADING')

  //   api.editCustomer(payload)
  //     .then(recipe => {
  //       context.commit('EDIT_CUSTOMER', recipe)
  //       context.commit('SET_CUSTOMER_DEFAULT')
  //       context.commit('TOGGLE_EDITTING')
  //       context.commit('TOGGLE_EDITFORM', false)
  //       context.commit('SUCCESS')
  //     })
  //     .catch(e => {
  //       context.commit('ERROR', e)
  //     })
  // },
  // deleteCustomer(context, payload) {
  //   context.commit('LOADING')

  //   Request.deleteCustomer(payload)
  //     .then(res => {
  //       if (res.status === 200) {
  //         context.commit('DELETE_CUSTOMER', payload)
  //         context.commit('SUCCESS')
  //       } else {
  //         context.commit('ERROR', res)
  //       }
  //     })
  //     .then(e => {
  //       context.commit('ERROR', e)
  //     })
  // },
  // clearError(context) {
  //   context.commit('CLEAR_ERROR')
  // },
  // setEditForm(context, payload) {
  //   context.commit('TOGGLE_EDITFORM', payload)
  // },
  // toggleEditting(context) {
  //   context.commit('TOGGLE_EDITTING')
  // },
  // paginate(context, payload) {
  //   context.commit('PAGINATE', payload)
  //   context.dispatch('getCustomers')
  // }
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
