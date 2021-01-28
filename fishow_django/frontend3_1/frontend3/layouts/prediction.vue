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
import LoginModal from '@/components/Header/LoginModal'
import RegModal from '@/components/Header/RegModal'
import HeaderBlock from '@/components/HeaderBlock'
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
import urlData from '~/assets/mixins/prediction/urlData'

import TheFooter from '~/components/TheFooter'
import SideBar from '~/components/predictPage/Menu/SideBar'

import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
import FPBreadCrumbs from '~/components/predictPage/Menu/FPBreadCrumbs'
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
