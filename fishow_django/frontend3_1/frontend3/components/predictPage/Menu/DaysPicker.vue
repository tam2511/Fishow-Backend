<template>
  <div class="data-pick">
    <div v-for="day in tenDays" :key="day.id" class="tenDays">
      <nuxt-link
        :to="{
          name: 'OnePrediction-areal-date-city-fish',
          params: {
            areal: $route.params.areal,
            date: '2020-' + day.split('/')[1] + '-' + day.split('/')[0],
            city: $route.params.city,
            fish: $route.params.fish,
          },
        }"
      >
        {{ day }}
      </nuxt-link>
    </div>
    <!--    <b-pagination-->
    <!--      :total="total"-->
    <!--      :current.sync="current"-->
    <!--      :range-before="rangeBefore"-->
    <!--      :range-after="rangeAfter"-->
    <!--      :order="order"-->
    <!--      :size="size"-->
    <!--      :simple="isSimple"-->
    <!--      :rounded="isRounded"-->
    <!--      :per-page="perPage"-->
    <!--      :icon-prev="prevIcon"-->
    <!--      :icon-next="nextIcon"-->
    <!--      aria-next-label="Next page"-->
    <!--      aria-previous-label="Previous page"-->
    <!--      aria-page-label="Page"-->
    <!--      aria-current-label="Current page"-->
    <!--    >-->
    <!--    </b-pagination>-->
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
  data() {
    return {
      total: 200,
      current: 10,
      perPage: 10,
      rangeBefore: 2,
      rangeAfter: 1,
      order: 'is-centered',
      size: '',
      isSimple: false,
      isRounded: false,
      prevIcon: 'chevron-left',
      nextIcon: 'chevron-right',
    }
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
.tenDays a {
  color: #fff;
  padding: 10px;
  background-color: #00000040;
  cursor: pointer;
  display: inline-block;
  /*margin: 5px 5px;*/
  /*border-radius: 5px;*/
  &:hover {
    background-color: #00b3ee;
  }
}
</style>
