<template>
  <b-carousel-list
    v-model="test"
    :data="items"
    :items-to-show="countFish"
    class="box"
  >
    <template slot="item" slot-scope="props">
      <div class="card">
        <div class="card-image">
          <figure class="image is-5by4">
            <a @click="info(props.index)"><img :src="props.list.image" /></a>
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
</template>

<script>
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
      test: 0,
      items: [
        {
          title: 'щука',
          image:
            'http://zoogalaktika.ru/assets/images/pisces/esociformes/esox-lucius/small/esox-lucius_small_02.jpg',
        },
        {
          title: 'судак',
          image:
            'https://avatars.mds.yandex.net/get-pdb/225396/82c64f8f-ce07-45c4-a83a-ba850870bf3b/s375',
        },
        {
          title: 'окунь',
          image:
            'https://im0-tub-ru.yandex.net/i?id=ca54386da6bcdf1319b513d9aaa9ecd1&n=13&exp=1',
        },
        {
          title: 'берш',
          image: 'https://fb.ru/misc/i/gallery/11538/496828.jpg',
        },
        {
          title: 'речная форель',
          image:
            'https://im0-tub-ru.yandex.net/i?id=f211f2c80dc4d056994345f681d0b8e8-sr&n=13&exp=1',
        },
        {
          title: 'озерная форель',
          image: 'https://dikiymir.ru/images/stories/azbuka/ff/forel.jpg',
        },
        {
          title: 'елец',
          image:
            'https://im0-tub-ru.yandex.net/i?id=80d5059428aec2eec7aad944752c1cb0-sr&n=13&exp=1',
        },
        {
          title: 'чехонь',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'сом',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'голавль',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'карп',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'жерех',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'лещ',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'карась',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'линь',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'пескарь',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'ротан',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'плотва',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'красноперка',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'налим',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'густера',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'амур',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'ерш',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'сазан',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'толстолобик',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'вобла',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
      ],
    }
  },
  computed: {
    countFish() {
      if (process.browser) {
        if (document.documentElement.clientWidth < 768) {
          return 2
        } else {
          return 5
        }
      } else return 4
    },
    list() {
      return this.fishList.filter(
        (fish, index) => index > this.first - 9 && index < this.first
      )
    },
  },
  methods: {
    info(value) {
      this.test = value
    },
  },
}
</script>

<style scoped lang="scss">
.fish-select-body {
  display: flex;
  flex-flow: row;
  max-width: 640px;
  margin: auto;
}
.fish-container {
  max-height: 150px;
  display: flex;
  padding: 0 50px;
  &-item {
    width: 80px;
    height: 80px;
    cursor: pointer;
    transition: 0.3s;
    margin: 20px;
    border-radius: 25px;
    position: relative;
    background-color: rgba(0, 0, 0, 0.3);
    &_value {
      position: absolute;
      transform: translate(-50%, -50%);
      left: 50%;
      top: 50%;
      margin: 0;
      text-align: center;
    }
    &:hover {
      color: #ffffff;
      background-color: cadetblue;
    }
  }
}
</style>
