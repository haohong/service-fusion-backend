export default {
  methods: {
    formatAddress: address => {
      const { address1, address2, city, state, country, zip_code } = address

      return `${address1} ${address2} ${city} ${state} ${country} ${zip_code}`
    }
  }
}
