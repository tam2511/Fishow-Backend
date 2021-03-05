<template>
  <div class="box fish">
    <div class="fish-select">
      <div class="fish-select_item fish-select_item__right">
        <fish-select @select="selectFish" />
      </div>
    </div>
    <b-carousel-list
      v-if="!passive"
      id="experience"
      v-model="fishId"
      :data="fishList"
      :items-to-show="countFish"
    >
      <template slot="item" slot-scope="props">
        <div class="card" @click="info(props)">
          <div class="card-image">
            <figure class="image is-5by4">
              <a> <img :src="props.list.image" alt="" /></a>
            </figure>
          </div>
          <div class="card-content content_fish-name">
            <div class="content">
              <h6 class="title is-6">{{ props.list.title }}</h6>
            </div>
          </div>
        </div>
      </template>
    </b-carousel-list>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import fishList from '~/assets/data/fishList'
import FishSelect from '~/components/predictPage/Menu/FishSelect'
export default {
  components: { FishSelect },
  props: {
    areal: {
      type: String,
      required: false,
      default: 'Московская область',
    },
    city: {
      type: String,
      required: false,
      default: 'Москва',
    },
    date: {
      type: String,
      required: true,
    },
    passive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      fishList,
      selectedFish: null,
      first: 5,
      data: 0,
    }
  },
  computed: {
    countFish() {
      if (process.browser) {
        if (document.documentElement.clientWidth < 768) {
          return 2
        } else {
          return 4
        }
      } else return 4
    },
    fish() {
      return this.fishList[this.data].title
    },
    ...mapState('prediction', ['fishId', 'multiPrediction']),
  },
  watch: {
    fishId(val) {
      this.selectedFish = val
    },
  },
  methods: {
    info(value) {
      this.setFish(value.index)
      this.selectFish(value.title)
    },
    selectFish(value) {
      let id = 0
      this.fishList.forEach((item, index) => {
        if (item.title === value) id = index
      })
      this.setFish(id)
      const fish = value
      const date = this.date
      const city = this.city
      const areal = this.areal
      let url
      if (this.multiPrediction) {
        url = encodeURI(
          `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
        )
      } else {
        url = encodeURI(
          `/prediction/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
        )
      }

      if (this.multiPrediction) {
        this.getPrediction(url)
      } else {
        this.getPredictionOne(url)
      }
    },
    ...mapActions('prediction', {
      setFish: 'setFishId',
      getPrediction: 'getPrediction',
      getPredictionOne: 'getPredictionOne',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
}
</script>

<style lang="scss">
.carousel-slide {
  transition: background-color 0.3s;
  cursor: pointer;
  &.is-active {
    background-color: #30bab5;
  }
  &:hover {
    background-color: #30bab5;
  }
}
.content_fish-name {
  padding: 1px;
  background-color: #5b714685;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  .title.is-6 {
    text-transform: capitalize;
    text-align: center;
    font-size: 20px;
    margin: 10px;
    font-weight: initial;
    color: #fff;
  }
}
.box.fish {
  padding-top: 0;
  background: none;
  border: none;
  box-shadow: none;
  span.select,
  span.select > select {
    width: 100%;
  }
}
</style>
