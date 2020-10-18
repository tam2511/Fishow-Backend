<template lang="pug">
  #app
    HeaderBlock
    .columns
      .column.is-three-quarters
        .container.main-content
          FPBreadCrumbs(
            :areal="areal",
            :city="city",
            :fish="fish",
            :date="date",
            )
          FishowPredictionHeader
            DaysPicker(
              :days="date"
              )
          FishSelectPrediction(
            :areal="areal",
            :city="city",
            :date="date",
          )
          nuxt
      .column.pSideBar
        SideBar
    TheFooter
    LoginModal(v-if="showStateLogin")
    RegModal(v-if="showStateReg")
</template>
<script>
import { mapState } from 'vuex'
import urlData from '~/assets/mixins/prediction/urlData'

import LoginModal from '@/components/Header/LoginModal'
import RegModal from '@/components/Header/RegModal'
import HeaderBlock from '@/components/HeaderBlock'
import TheFooter from '~/components/TheFooter'
import SideBar from '~/components/predictPage/Menu/SideBar'

import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
import FPBreadCrumbs from '~/components/predictPage/Menu/FPBreadCrumbs'
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
export default {
  components: {
    SideBar,
    HeaderBlock,
    LoginModal,
    RegModal,
    TheFooter,
    FPBreadCrumbs,
    DaysPicker,
    FishSelectPrediction,
    FishowPredictionHeader,
  },
  mixins: [urlData],
  computed: {
    ...mapState('login', ['showStateLogin', 'showStateReg']),
  },
}
</script>
<style lang="scss">
body {
  background-color: #eee;
}
.results-container .columns {
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
}
a {
  color: #0d0a0a;
  transition: color 0.3s;
  &:hover {
    color: rgba(0, 0, 0, 0.55);
  }
}
.column.pSideBar {
  position: fixed;
  right: 0;
  width: 25%;
  top: 55px;
  min-height: 500px;
  height: calc(100% - 250px);

  @media screen and (max-width: 768px) {
    display: none;
  }
}
.header {
  @media screen and (max-width: 450px) {
    width: 100%;
  }
}
div.container {
  @media screen and (max-width: 450px) {
    padding-right: 0;
  }
}
.blue {
  color: #09438e;
}
.red {
  color: #8a0000;
}
.green {
  color: green;
}
.strong {
  font-weight: 800;
}
.report-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  span {
    height: 6rem;
    width: 6rem;
    i {
      font-size: 6rem;
      color: #fff;
    }
  }
}
@media screen and (max-width: 450px) {
  .column.is-three-quarters {
    padding-left: 0;
    padding-right: 0;
  }
}
@media screen and (min-width: 769px) {
  .main-content {
    padding-left: 20px;
  }
}
</style>
