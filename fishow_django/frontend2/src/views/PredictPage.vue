<template>
  <section class="section section-variant-1 bg-gray-100">
    <div
      class="container container__small"
      :class="step < 3 ? 'container__small_menu' : 'hideMenu'"
    >
      <div v-if="step < 3" class="select-predict">
        <el-steps :active="step" finish-status="success">
          <el-step title="Область"></el-step>
          <el-step title="Населенный пункт"></el-step>
          <el-step title="Рыба"></el-step>
        </el-steps>
        <div v-if="step === 0">
          <el-select v-model="value" placeholder="Select">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
        <div v-else-if="step === 1">
          <el-select v-model="value2" placeholder="Select">
            <el-option
              v-for="item in options2[`${this.value}`]"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
        <div v-else-if="step === 2">
          <fish-search @data="onChange" />
        </div>
        <h4>Область: {{ getOblast }}</h4>
        <h4>Город: {{ getCity }}</h4>
        <h4>Рыба: {{ getFish }}</h4>
        <h4>Шаг: {{ step }}</h4>
        <h6 style="color: red;">{{ error }}</h6>

        <div class="predict_footer">
          <el-button @click="fullBack">В начало</el-button>
          <el-button @click="back">Назад</el-button>
          <el-button @click="next">Дальше</el-button>
        </div>
      </div>
      <div v-else class="predict">
        <span
          >{{ this.value }} / {{ this.value2 }} | Прогноз на близжайшие 10 дней
          - {{ this.fish }}</span
        >
        <column :action="loadingfunc()" />
        <div class="predict_footer">
          <el-button @click="back">Назад</el-button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import fishSearch from '../components/predictPage/fishSearch'
import Column from '../components/predictPage/column'
import { Loading } from 'element-ui'

export default {
  name: 'PredictPage',
  components: { Column, fishSearch },
  data() {
    return {
      result: '',
      data: {
        temperature_min: '[1,2,1,3,1,2,3,2,4]',
        temperature_mean: '[2,3,2,3,3,4,5,4,3]',
        temperature_max: '[4,5,4,5,5,4,6,7,8]',
        wind_mean: '[3,6,5,7,3,4,6,3,2]',
        wind_direction: '["СЗ","З","З","СЗ","С","В","Ю","ЮВ","В"]',
        gust_max: '[7,13,5,11,11,10,9,10,10]',
        phenomenon:
          '["[пасмурно]","[дождь,малооблачно]","[малооблачно]","[дождь,пасмурно]","[ясно]","[пасмурно]","[пасмурно]","[ясно]","[пасмурно]"]',
        pressure_min: '[733,734,733,735,735,733,738,735,733]',
        pressure_max: '[739,740,739,751,739,744,746,744,739]',
        humidity_mean: '[64,63,22,34,44,71,33,54,57]',
        uv_index_mean: '[3,3,3,3,5,4,3,2,1]',
        moon: '[1,4,7,14,21,28,33,40]',
        moon_direction: '[1,1,1,1,1,1,1,1,1]',
        date: '04.04.2020',
        areal: 'московскаяобласть',
        city: 'москва',
        fish: 'щука',
        prob_min: '[0.1,0.2,0.1,0.5,0.3,0.5,0.2,0.3,0.2]',
        prob_max: '[0.2,0.5,0.3,0.8,0.6,0.8,0.5,0.7,0.6]',
      },
      options: [
        {
          value: 'Московская область',
          label: 'Московская область',
        },
        {
          value: 'Ленинградская обл',
          label: 'Ленинградская обл',
        },
      ],
      options2: {
        'Московская область': [
          {
            value: 'москва',
            label: 'Москва',
          },
          {
            value: 'Балашиха',
            label: 'Балашиха',
          },
        ],
        'Ленинградская обл': [
          {
            value: 'СПБ',
            label: 'Санкт-Петербург',
          },
          {
            value: 'Светогорск',
            label: 'Светогорск',
          },
        ],
      },
      activeName: 'first',
      value: '',
      value2: '',
      value3: '',
      loading: true,
      step: 0,
      error: '',
      fish: '',
      showMenu: false,
    }
  },
  computed: {
    getStep() {
      let value = 0
      console.log(this.value)
      if (this.value !== '') value = 1
      if (this.value2 !== '') value = 2
      if (this.value3 !== '') {
        this.loadingfunc()
        value = 3
      }
      return value
    },
    getOblast() {
      return this.value
    },
    getCity() {
      return this.value2
    },
    getFish() {
      return this.fish
    },
    maxWidth() {
      return this.step <= 2 ? 'max-width: 500px' : 'max-width: 70%'
    },
  },
  methods: {
    onChange(data) {
      this.fish = data.value
    },
    // errorMesage() {
    //   this.$message({
    //     message: 'Ошибка: Сперва выберите параметр',
    //     type: 'error',
    //   })
    // },
    next() {
      if (this.value) {
        this.step = 1
        if (this.value && this.value2) {
          this.step = 2
          if (this.value && this.value2 && this.fish) {
            this.step = 3
            this.loadingfunc()
          }
        }
      } else {
        // this.errorMesage()
      }
    },
    back() {
      this.loading = true
      if (this.step > 0) {
        this.step -= 1
      }
      this.result = ''
    },
    fullBack() {
      this.value = ''
      this.value2 = ''
      this.value3 = ''
      this.fish = ''
      this.step = 0
    },
    handleChange(value) {
      console.log(value)
    },
    loadingfunc() {
      const options = {
        target: document.querySelector('body'),
        fullscreen: true,
        lock: true,
        background: 'rgba(24,99,107,0.98)',
      }
      let loadingInstance = Loading.service(options)
      setTimeout(() => {
        document.querySelector('.container__small').classList.remove('hideMenu')
        loadingInstance.close()
      }, 2000)
    },
  },
  created() {
    this.data.temperature_max = this.data.temperature_max
      .slice(1, this.data.temperature_max.length - 1)
      .split(',')

    Object.keys(this.data).forEach((key) => {
      if (this.data[key][0] === '[') {
        this.data[key] = this.data[key]
          .slice(1, this.data[key].length - 1)
          .split(',')
      }
      console.log(key, ' ', this.data[key])
    })
  },
}
</script>

<style scoped lang="scss">
.section.section-variant-1 {
  overflow-scrolling: auto;
  overflow: scroll;
  overflow-y: auto;
}
.el-cascader {
  margin: 20px 0;
  display: block;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border: 1px solid rgba(0, 0, 0, 0.2);
  min-height: 70px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.container__small {
  opacity: 1;
  max-width: 900px;
  padding: 20px;
  border: none;
  min-height: 500px;
  background-color: #fff;
  &_menu {
    max-width: 500px;
  }
  transition: all 0.3s;

  @media screen and (max-width: 600px) {
    width: 1024px !important;
    max-height: 100% !important;
  }
}
.hideMenu {
  opacity: 0;
}
.predict,
.select-predict {
  position: relative;
  min-height: 458px;
}
.predict_footer {
  position: absolute;
  bottom: 0;
  right: 0;
  button {
    border: none;
    transition-duration: 0.2s;
    box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
    &:hover {
      transition-duration: 0.2s;
      box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
      background-color: #ffd851;
      color: #000;
    }
  }
}
.el-select {
  display: block;
  padding: 20px 0;
}
</style>
