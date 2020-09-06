<template>
  <div class="box fish">
    <div class="columns">
      <div class="column is-two-thirds">
        <p class="content"></p>
      </div>
      <div class="column">
        <b-field>
          <b-select placeholder="Выберите рыбу">
            <option
              v-for="(fishs, index) in fishList"
              :key="fishs.id"
              :value="fishs.id"
              @click="info(index)"
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
        <div class="card" @click="info(props.index)">
          <div class="card-image">
            <figure class="image is-5by4">
              <a> <img :src="props.list.image" /></a>
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
      rawHtml:
        '<strong>Lorem ipsum dolor sit amet</strong>, consectetur *adipiscing elit*, sed do eiusmod tempor incididunt ut <strong>labore</strong> et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco *laboris nisi ut aliquip* ex ea commodo consequat. <strong>uis aute irure dolor <span class="red">in reprehenderit in voluptate velit esse cillum</strong></span>',
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
