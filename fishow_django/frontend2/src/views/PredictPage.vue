<template>
  <section class="section section-variant-1 bg-gray-100">
    <div class="container container__small" :style="maxWidth">
      <!--            <div v-if="getStep < 3" class="select-predict">-->
      <div v-if="step < 3" class="select-predict">
        <el-steps :active="step" finish-status="success">
          <el-step title="Область"></el-step>
          <el-step title="Населенный пункт"></el-step>
          <el-step title="Рыба"></el-step>
        </el-steps>

        <!--                <el-cascader @change="handleChange" v-model="value" :options="options" placeholder="Ваш выбор" clearable></el-cascader>-->

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
      <div v-else class="predict" v-loading="loading">
        <h4>{{this.value}} / {{this.value2}}</h4>
        <h4>Прогноз на близжайшие 10 дней - {{ this.fish }}</h4>
        <el-tabs v-model="activeName">
          <el-tab-pane
            v-for="day in days"
            :key="day.id"
            :label="day.name"
            :name="day.label"
          >
            <column />
          </el-tab-pane>
        </el-tabs>
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
export default {
  name: 'PredictPage',
  components: { Column, fishSearch },
  data() {
    return {
      days: [
        {
          name: 'Понедельник',
          label: 'first',
        },
        {
          name: 'Вторник',
          label: 'first2',
        },
        {
          name: 'Среда',
          label: 'first3',
        },
        {
          name: 'Четверг',
          label: 'first4',
        },
        {
          name: 'Пятница',
          label: 'first5',
        },
        {
          name: 'Суббота',
          label: 'first6',
        },
        {
          name: 'Воскресенье',
          label: 'first7',
        },
      ],
      result: '',
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
    errorMesage() {
      this.$message({
        message: 'Ошибка: Сперва выберите параметр',
        type: 'error',
      })
    },
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
        this.errorMesage()
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
      this.step = 0
    },
    handleChange(value) {
      console.log(value)
    },
    loadingfunc() {
      setTimeout(() => {
        this.loading = false
      }, 2000)
    },
  },
}
</script>

<style scoped lang="scss">
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
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
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
  max-width: 500px;
  padding: 20px;
  border: none;
  min-height: 500px;
  background-color: #fff;
  transition: all 0.3s;
  &:hover {
    box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
  }
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
}
.el-select {
  display: block;
  padding: 20px 0;
}
</style>
