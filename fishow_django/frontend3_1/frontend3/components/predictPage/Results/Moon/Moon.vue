<template lang="pug">
  .moon-box.box
    h3.title Луна
    .columns.moons
      MoonOne.column(v-for="(day, index) in readyDataStorage" :key="day.date + index" :day="day")
    .columns.moon-columns
      .column.moon-pic
        figure.image
          img(src="/image 92.png" alt="a random image" ratio="6by4")
      .column.moon_desc
        p(v-html="readyDataStorage.moon_desc.bad" data-status="bad")
        p(v-html="readyDataStorage.moon_desc.neutral" data-status="neutral")
        p(v-html="readyDataStorage.moon_desc.good" data-status="good")
</template>

<script>
import readyDataStorage from '~/assets/mixins/prediction/readyDataStorage'
import MoonOne from '~/components/predictPage/Results/Moon/OneDay/MoonOne'
export default {
  components: {
    MoonOne,
  },
  mixins: [readyDataStorage],
}
</script>

<style scoped lang="scss">
.moon-box {
  padding-bottom: 50px;
}
.moons {
  padding-bottom: 50px;
}
@media screen and (max-width: 768px) {
  div.columns {
    display: flex;
    overflow: scroll;
    min-height: 200px;
  }
  .moon-columns {
    flex-flow: column;
  }
  .moon-pic {
    min-width: 300px;
  }
}
.moons div.column {
  display: flex;
  align-items: center;
  flex-flow: column;
}
.moon_desc {
  display: flex;
  flex-flow: column;
  justify-content: center;
  @media screen and (max-width: 450px) {
    width: 90%;
    margin-left: auto;
  }
  p {
    position: relative;
    padding: 5px 0;
  }
  p:before {
    position: absolute;
    top: 50%;
    left: -20px;
    content: '•';
    font-size: 5rem;
    line-height: 10px;
    transform: translate(-50%, -50%);
  }
  [data-status='bad']:before {
    color: darkred;
  }
  [data-status='good']:before {
    color: #22a022;
  }
  [data-status='neutral']:before {
    color: #b6b60a;
  }
}
.image img {
  margin: 0 auto;
}
.moon-pic {
  margin-right: 40px;
  max-width: 400px;
}
</style>
