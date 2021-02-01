<script>
export default {
  name: 'FetchData',
  props: {
    endpoint: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      response: [],
    }
  },
  created() {
    this.$axios
      .get(this.endpoint)
      .then((response) => {
        this.response = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  render() {
    return this.$scopedSlots.default({
      response: this.response,
    })
  },
}
</script>
