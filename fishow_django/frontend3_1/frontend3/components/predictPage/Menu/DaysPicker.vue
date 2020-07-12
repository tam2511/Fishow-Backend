<template>
  <div class="data-pick">
    <div v-for="day in tenDays" :key="day.id" class="tenDays">
      {{ day }}
    </div>
  </div>
</template>

<script>
import getData from '~/assets/js/getData'
export default {
  props: {
    days: {
      type: String,
      required: true,
    },
  },
  computed: {
    tenDays() {
      return getData(this.days, 9)
    },
  },
}
</script>

<style scoped lang="scss">
.data-pick {
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
}
.is-link {
  background-color: #204a6f85;
}
.tenDays {
  color: #fff;
  padding: 2px 5px;
  background-color: #00000040;
  cursor: pointer;
  margin: 5px 5px;
  border-radius: 5px;
  &:hover {
    background-color: #00b3ee;
  }
}
</style>
