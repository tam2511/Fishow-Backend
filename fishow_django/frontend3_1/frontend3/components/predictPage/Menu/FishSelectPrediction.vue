<template>
  <div class="box fish">
    <div class="columns">
      <div class="column is-two-thirds">
        <p class="content">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
      </div>
      <div class="column">
        <b-field>
          <b-select placeholder="Select a name">
            <option
              v-for="(fishs, index) in fishList"
              :key="fishs.id"
              @click="info(index)"
              :value="fishs.id"
            >
              {{ fishs.title }}
            </option>
          </b-select>
        </b-field>
      </div>
    </div>
    <b-carousel-list
      id="experience"
      v-model="fishId"
      :data="fishList"
      :items-to-show="countFish"
    >
      <template slot="item" slot-scope="props">
        <div class="card">
          <div class="card-image">
            <figure class="image is-5by4">
              <a @click="info(props.index)"> <img :src="props.list.image" /></a>
            </figure>
          </div>
          <div class="card-content">
            <div class="content">
              <p class="title is-6">{{ props.list.title }}</p>
            </div>
          </div>
        </div>
      </template>
    </b-carousel-list>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  props: {
    areal: {
      type: String,
      required: true,
    },
    city: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      first: 5,
      data: 0,
      fishList: [
        { title: 'щука', image: '/fish_green/щука.jpg' },
        { title: 'судак', image: '/fish_green/судак.jpg' },
        { title: 'окунь', image: '/fish_green/окунь.jpg' },
        { title: 'берш', image: '/fish_green/берш.jpg' },
        { title: 'речная форель', image: '/fish_green/речная форель.jpg' },
        { title: 'озерная форель', image: '/fish_green/озерная форель.jpg' },
        { title: 'елец', image: '/fish_green/елец.jpg' },
        { title: 'чехонь', image: '/fish_green/чехонь.jpg' },
        { title: 'сом', image: '/fish_green/сом.jpg' },
        { title: 'голавль', image: '/fish_green/голавль.jpg' },
        { title: 'язь', image: '/fish_green/язь.jpg' },
        { title: 'карп', image: '/fish_green/карп.jpg' },
        { title: 'жерех', image: '/fish_green/жерех.jpg' },
        { title: 'лещ', image: '/fish_green/лещ.jpg' },
        { title: 'карась', image: '/fish_green/карась.jpg' },
        { title: 'линь', image: '/fish_green/линь.jpg' },
        { title: 'пескарь', image: '/fish_green/пескарь.jpg' },
        { title: 'ротан', image: '/fish_green/ротан.jpg' },
        { title: 'плотва', image: '/fish_green/плотва.jpg' },
        { title: 'красноперка', image: '/fish_green/красноперка.jpg' },
        { title: 'налим', image: '/fish_green/налим.jpg' },
        { title: 'густера', image: '/fish_green/густера.jpg' },
        { title: 'амур', image: '/fish_green/амур.jpg' },
        { title: 'ерш', image: '/fish_green/ерш.jpg' },
        { title: 'сазан', image: '/fish_green/сазан.jpg' },
        { title: 'подуст', image: '/fish_green/подуст.jpg' },
        { title: 'толстолобик', image: '/fish_green/толстолобик.jpg' },
        { title: 'вобла', image: '/fish_green/вобла.jpg' },
      ],
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
    ...mapState('prediction', ['fishId']),
  },
  methods: {
    info(value) {
      const fish = this.fishList[value].title
      const date = this.date
      const city = this.city
      const areal = this.areal
      const url = encodeURI(
        `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
      )

      this.setFish(value)
      this.getPrediction(url)
      // this.$refs.pprobe.updateData()
    },
    ...mapActions('prediction', {
      setFish: 'setFishId',
      getPrediction: 'getPrediction',
    }),
  },
}
</script>

<style lang="scss">
.carousel-slide.is-active {
  background-color: #00b3ee;
}
</style>
