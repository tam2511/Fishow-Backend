<template lang="pug">
  .moon-container
    .moon-main
      figure.image.is-48x48
        img(:src="moonPic")
        p.content {{ moon.toFixed() }}%
    .sun-info__container
      .sun-info__inner.sun-info__inner_up
        .sun-info__item_header
          span Восход
          span {{ sunUp }}
        .sun-info__item_body
          span Солнца
        .sun-info__item_footer
          span {{ date }}, днем
      .sun-info__inner.sun-info__inner_down
        .sun-info__item_header
          span Заход
          span {{ sunDown }}
        .sun-info__item_body
          span Солнца
        .sun-info__item_footer
          span {{ date }}, ночью
    .moon-desc
      .moon-desc_item(v-html="moonDesc")
</template>

<script>
export default {
  props: {
    moon: {
      type: Number,
      required: true,
    },
    moonDesc: {
      type: String,
      required: true,
    },
    moonDir: {
      type: Number,
      required: true,
    },
    sunUp: {
      type: String,
      required: true,
    },
    sunDown: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
  computed: {
    moonPic() {
      const pic = {
        1: {
          0: '/assets/moon/1.png',
          10: '/assets/moon/2.png',
          20: '/assets/moon/3.png',
          30: '/assets/moon/4.png',
          40: '/assets/moon/5.png',
          50: '/assets/moon/6.png',
          60: '/assets/moon/7.png',
          70: '/assets/moon/8.png',
          80: '/assets/moon/9.png',
          90: '/assets/moon/10.png',
          100: '/assets/moon/11.png',
        },
        '-1': {
          0: '/assets/moon/23.png',
          10: '/assets/moon/22.png',
          20: '/assets/moon/21.png',
          30: '/assets/moon/20.png',
          40: '/assets/moon/19.png',
          50: '/assets/moon/18.png',
          60: '/assets/moon/17.png',
          70: '/assets/moon/16.png',
          80: '/assets/moon/15.png',
          90: '/assets/moon/14.png',
          100: '/assets/moon/13.png',
        },
      }
      let result = 0
      result = pic[this.moonDir]
      for (const one in result) {
        if (this.moon >= one) {
          result = one
        }
      }
      return (
        (pic[this.moonDir] && pic[this.moonDir][result]) ||
        '/assets/moon/23.png'
      )
    },
  },
}
</script>

<style scoped lang="scss">
.moon-container {
  display: flex;
  flex-flow: row;
  justify-content: space-between;
  align-items: center;

  & > div {
    flex: 0 1 33%;
    @media screen and (max-width: 768px) {
      margin-top: 30px;
    }
  }
  & > div:first-child {
    flex: 0 1 10%;
  }
}

.sun-info__container {
  display: flex;
  flex-flow: row;
  justify-content: center;
  align-items: center;
  @media screen and (max-width: 768px) {
    flex-wrap: wrap;
    text-align: center;
  }
}
.sun-info__item_header {
  font-size: 2.5rem;
  span:first-child {
    padding-right: 10px;
  }
}
.sun-info__item_body {
  font-size: 1.5rem;
}

.sun-info__inner:not(:last-child) {
  @media screen and (min-width: 768px) {
    margin-right: 20px;
  }
  @media screen and (max-width: 768px) {
    margin-top: 20px;
    text-align: center;
  }
}
.sun-info__inner_up {
  .sun-info__item_header span:first-child {
    color: #995315;
    /*color: #b0e4e8;*/
  }
}
.sun-info__inner_down {
  .sun-info__item_header span:first-child {
    /*color: #d5e7c9;*/
    color: #20757b;
  }
}

.moon-main {
  .image {
    width: 80px;
    height: 80px;
    margin: 0 auto;
  }
  .content {
    text-align: center;
    margin-top: 10px;
  }
}

@media screen and (max-width: 720px) {
  .moon-container {
    flex-flow: column;
    width: 100%;
  }
}
</style>
