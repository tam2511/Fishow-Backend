import PredictionService from '~/services/PredictionService'
// eslint-disable-next-line no-unused-vars
const defaultPred = {
  template: 'template',
  id: 2,
  temperature_min: [1, 2, 4, 2, 0, 3, 2, -2, -2],
  temperature_max: [10, 14, 14, 12, 3, 4, 6, 1, 3],
  wind_mean: [2, 2, 2, 3, 5, 4, 2, 5, 2],
  wind_direction: ['Ю', 'Ю', 'Ю', 'ЮВ', 'ЮЗ', 'Ю', 'ЮВ', 'ЮЗ', 'ЮЗ'],
  gust_max: [7, 8, 10, 12, 15, 13, 10, 16, 12],
  phenomenon: [
    'пасмурно',
    'ясно',
    'ясно',
    'пасмурно,небольшой дождь',
    'пасмурно',
    'пасмурно,небольшой дождь',
    'пасмурно,небольшой дождь',
    'пасмурно,небольшой снег',
    'пасмурно,небольшой снег',
  ],
  pressure_min: [749, 746, 744, 740, 745, 743, 740, 743, 749],
  pressure_max: [752, 749, 746, 743, 747, 745, 744, 748, 755],
  humidity_mean: [70, 70, 75, 77, 65, 80, 89, 77, 71],
  uv_index_mean: [2, 3, 2, 2, 1, 1, 1, 1, 0],
  moon: [98, 94, 89, 82, 74, 65, 56, 45, 35],
  moon_direction: [-1, -1, -1, -1, -1, -1, -1, -1, -1],
  prob_min: [40, 35, 36, 31, 38, 45, 40, 31, 21],
  prob_max: [40, 45, 47, 49, 60, 70, 62, 51, 41],
  temperature_brief:
    'Температура воздуха оказывает значительное влияние на клев в случае резких перепадов температуры. В случае небольших изменений температуры воздуха при прогнозе клева <strong>щуки</strong> учитывается влияние других факторов. ',
  temperature_fish:
    'На <strong>щуку</strong> положительно влияет <span class="blue strong">понижение</span> температуры воздуха, а ее резкое <span class="red strong">повышение</span> способствует уменьшению активности рыбы. ',
  temperature_desc: {
    desc:
      '<strong>4 октября-6 октября и 8 октября-9 октября</strong> ожидается резкое <span class="blue strong">понижение</span> температуры воздуха. <strong>2 октября-3 октября</strong> прогнозируется резкое <span class="red strong">повышение</span> температуры воздуха. ',
    day: {
      mean: 5.814814814814815,
      min: -1,
      max: 14,
      min_date: '9 октября',
      max_date: '3 октября',
    },
    night: {
      mean: 2.111111111111111,
      min: -1,
      max: 7,
      min_date: '9 октября',
      max_date: '5 октября',
    },
  },
  phenomenon_warning:
    'На данный момент для определения степени влияния погодных явлений на клев <strong>щуки</strong> в данном регионе необходимо больше данных. Вы можете <strong>оставить отчет</strong> о рыбалке в Кемеровская область и помочь выявить закономерности нашему алгоритму. ',
  prediction_brief:
    'Прогноз клева <strong>щуки</strong> рассчитан на основе всех погодных факторов за <strong>2 октября-10 октября</strong>. Если вероятность клева в интересующее Вас время больше 70%, то клев считается хорошим, если вероятность меньше 30%, то клев считается плохим, иначе клев является умеренный и успех рыбалки во многом зависит от вашего мастерства. ',
  prediction_desc: {
    min: '31 %',
    max: '84 %',
    min_date: '3 октября, вечером',
    max_date: '2 октября, днем',
  },
  wind_fish:
    'На данный момент, не известно как именно влияет сила и направление ветра на клев <strong>щуки</strong> . Однако, сильный <strong>северный</strong> или <strong>восточный</strong> ветер может испортить рыбалку.',
  wind_desc:
    '<strong>10 октября</strong> ожидается самая слабая за рассматриваемый период скорость ветра - <strong>2.125</strong> м/с, а <strong>6 октября</strong> возможнен сильный ветер - около <strong>5.625</strong> м/с. ',
  wind_roza: { З: 4, СЗ: 0, ЮЗ: 25, В: 0, СВ: 0, ЮВ: 12, Ю: 29, С: 0 },
  pressure_fish:
    'На <strong>щуку</strong> положительно влияет <span class="blue strong">спад</span> и <strong>стабильность</strong> атмосферного давления, а его резкий рост может негативно повлиять на активность рыбы. ',
  pressure_desc: {
    low_text:
      '<strong>2 октября-3 октября и 4 октября-5 октября</strong> ожидается резкий <span class="blue strong">спад</span> атмосферного давления. ',
    up_text:
      '<strong>5 октября-6 октября и 8 октября-10 октября</strong> прогнозируется резкий <span class="red strong">рост</span> атмосферного давления. ',
    max: 755,
    min: 740,
    min_date: '5 октября',
    max_date: '10 октября',
  },
  moon_desc: {
    bad:
      '<strong>2 октября-5 октября</strong> возможно ухудшение клева <strong>щуки</strong> по лунному календарю. ',
    neutral:
      '<strong>6 октября-8 октября</strong> луна не оказывает значительного влияния на клев рыбы. Стоит обратить внимание на другие факторы клева. ',
    good:
      '<strong>9 октября-10 октября</strong> луна находится в благоприятной стадии и способствуют хорошему клеву <strong>щуки</strong>. ',
  },
  uv_index_desc: {
    6: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    9: [1, 1, 1, 1, 0, 0, 0, 0, 0],
    12: [2, 3, 2, 2, 1, 1, 1, 1, 0],
    15: [1, 1, 1, 1, 0, 0, 0, 0, 0],
    18: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    21: [0, 0, 0, 0, 0, 0, 0, 0, 0],
  },
  date: '2020-10-02',
  areal: 'Кемеровская область',
  city: 'Белово',
  fish: 'щука',
}
export const state = () => ({
  fishId: 0,
  pageScroll: 0,
  predictions: null,
  prediction: null,
  readyDataStorage: null,
  days: null,
  multiPrediction: true,
  location: { areal: 'Московская область', city: 'Москва' },
})

export const mutations = {
  SET_FISHID(state, id) {
    state.fishId = id
  },
  SET_PREDICTIONTYPE(state, type) {
    state.multiPrediction = type
  },
  SET_READYDATA(state, data) {
    state.readyDataStorage = data
  },
  SET_DAYS(state, data) {
    state.days = data
  },
  SET_PREDICTIONS(state, predictions) {
    if (typeof predictions === 'undefined') {
      state.predictions = defaultPred
    } else {
      state.predictions = predictions
    }
  },
  SET_PREDICTION(state, prediction) {
    state.prediction = prediction
  },
  SET_LOCATION(state, location) {
    state.location = location
  },
}

export const actions = {
  setPredicitonType({ commit }, type) {
    commit('SET_PREDICTIONTYPE', type)
  },
  setFishId({ commit }, id) {
    commit('SET_FISHID', id)
  },
  setReady({ commit }, data) {
    commit('SET_READYDATA', data)
  },
  setDays({ commit }, days) {
    commit('SET_DAYS', days)
  },
  setLocation({ commit }, location) {
    commit('SET_LOCATION', location)
  },
  getPrediction({ commit, axios }, conf) {
    return PredictionService.getPredicitons(conf).then((response) => {
      commit('SET_PREDICTIONS', response.data.results[0])
    })
  },
  getPredictionOne({ commit, axios }, conf) {
    return PredictionService.getPredicitons(conf).then((response) => {
      commit('SET_PREDICTION', response.data.results[0])
    })
  },
}
