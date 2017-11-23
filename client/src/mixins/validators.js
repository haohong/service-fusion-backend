import isEmail from 'validator/lib/isEmail'

export default {
  data() {
    return {
      rules: {
        required: value => !!value || 'Required.',
        email: value => (!!value && isEmail(value)) || 'Invalid e-mail.',
        phoneNumber: value => {
          const regex = /^(\+\d{1,3})?\d{7,10}$/

          return (!!value && regex.test(value)) || 'Invalid phone number'
        },
        zipCode: value => {
          const regex = /^\d{4,9}$/

          return (!!value && regex.test(value)) || 'Invalid zip code'
        },
        maxLength: max => value =>
          (!!value && value.length <= max) ||
          `Must be ${max} characters or less`
      }
    }
  }
}
