import EmptyPrediction from '@/components/predictPage/EmptyPrediction'
import Wind from '@/components/predictPage/Results/Wind/index'
import Temperature from '~/components/predictPage/Results/Temperature/index'
import PressureContainer from '~/components/predictPage/Results/Pressure/PressureContainer'
import PressureChart from '~/components/predictPage/Results/Pressure/PressureChart'
import PProbe from '~/components/predictPage/Results/PProbe/index'
import ResultContainer from '~/components/predictPage/Results/resultContainer'
import Uvindexfull from '~/components/predictPage/Results/UVindex/uvindexfull'

export default {
  components: {
    ResultContainer,
    EmptyPrediction,
    PProbe,
    Temperature,
    PressureChart,
    PressureContainer,
    Wind,
    Uvindexfull,
  },
}
