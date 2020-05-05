<template>
  <div class="container container__small">
    <div class="select-predict">
      <el-steps :active="getStep" finish-status="success">
        <el-step title="Область"></el-step>
        <el-step title="Населенный пункт"></el-step>
        <el-step title="Рыба"></el-step>
      </el-steps>
      <div v-if="getStep === 0">
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
      <div v-else-if="getStep === 1">
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
      <div v-else-if="getStep === 2">
        <fish-search @data="onChange" />
      </div>
      <h6 style="color: red;">{{ error }}</h6>

      <div class="predict_footer">
        <el-button v-if="getStep > 0" @click="fullBack">В начало</el-button>
        <router-link
          :to="{
            name: 'PredictResult',
            params: {
              areal: getOblast,
              date: '2020-04-25',
              city: getCity,
              fish: getFish,
            },
          }"
          v-if="getStep === 3"
          ><el-button>Прогноз</el-button></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import fishSearch from '../components/predictPage/fishSearch'

export default {
  name: 'PredictPage',
  components: { fishSearch },
  data() {
    return {
      result: '',
      options: [
        {
          value: 'Московская область',
          label: 'Московская область',
        },
        {
          value: 'Ленинградская область',
          label: 'Ленинградская область',
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
        'Ленинградская область': [
          {
            value: 'санкт-петербург',
            label: 'Санкт-Петербург',
          },
          {
            value: 'светогорск',
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
      if (this.value !== '') value = 1
      if (this.value2 !== '') value = 2
      if (this.fish !== '') {
        value = 3
        this.route()
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
    route() {
      const someDate = new Date()
      const dd = someDate.getDate()
      const mm = someDate.getMonth() + 1
      const yy = someDate.getFullYear()
      const newmm = yy + '-' + mm + '-' + dd

      this.$router.push({
        name: 'PredictResult',
        params: {
          areal: this.getOblast,
          date: newmm,
          city: this.getCity,
          fish: this.getFish,
        },
      })
    },
    // errorMesage() {
    //   this.$message({
    //     message: 'Ошибка: Сперва выберите параметр',
    //     type: 'error',
    //   })
    // },
    fullBack() {
      this.value = ''
      this.value2 = ''
      this.value3 = ''
      this.fish = ''
      this.step = 0
    },
  },
  created() {
    document.title = 'Fishow - Прогноз'
  },
}
</script>

<style scoped lang="scss">
.section.section-variant-1 {
  @media screen and (max-width: 600px) {
    padding: 0;
  }
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
  max-width: 500px;
  padding: 20px;
  border: none;
  min-height: 500px;
  background-color: var(--background-color-primary);
  &_menu {
    max-width: 300px;
  }
  transition: all 0.3s;
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
div.el-step__title.is-process {
  color: var(--color-typo-primary) !important;
}
.el-select {
  display: block;
  padding: 20px 0;
}
</style>
