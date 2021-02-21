<template>
  <div class="tile container">
    <div class="tile is-vertical is-12">
      <h1 class="title">Написать отчет</h1>
      <div class="tile is-parent is-vertical box">
        <b-field>
          <b-input
            v-model="report.title"
            placeholder="Введите заголовок"
          ></b-input>
        </b-field>
        <div class="report-section">
          <section>
            <b-field>
              <b-datepicker
                v-model="report.date_start"
                placeholder="Начало рыбалки"
              >
              </b-datepicker>
            </b-field>
          </section>

          <section>
            <b-field>
              <b-datepicker
                v-model="report.date_end"
                placeholder="Конец рыбалки"
              >
              </b-datepicker>
            </b-field>
          </section>

          <section>
            <b-field>
              <b-input
                v-model="report.areal"
                placeholder="Укажите регион рыбалки"
              ></b-input>
            </b-field>
          </section>

          <section>
            <b-field>
              <b-input
                v-model="report.fishing"
                placeholder="Укажите водоем рыбалки"
              ></b-input>
            </b-field>
          </section>

          <section>
            <b-field>
              <b-input
                v-model="report.remark"
                placeholder="Укажите координаты места ловли"
              ></b-input>
            </b-field>
          </section>

          <section>
            <b-field>
              <b-input
                v-model="report.city"
                placeholder="Укажите ближайший город рыбалки"
              ></b-input>
            </b-field>
          </section>
        </div>
        <multiselect
          v-model="report_tags"
          tag-placeholder="Добавьте новый тег"
          placeholder="Найдите или добавьте свой тег"
          :options="options"
          :multiple="true"
          :taggable="true"
          @input="clearError"
          @tag="addTag"
        ></multiselect>
        <template v-for="(article, index) in articles">
          <component
            :is="article"
            :key="article[index] + index"
            :counter="article + index"
            @input.passive="fillBlog"
            @remove="removeElement"
          ></component>
        </template>
        <div class="buttons">
          <button
            v-for="button in buttons"
            :key="button.type"
            class="button button-primary button-sm"
            type="button"
            @click="addBlock(button.field)"
          >
            {{ button.type }}
          </button>
        </div>
        <div class="buttons">
          <button
            class="button is-success"
            type="button"
            name="send_blog"
            @click="onSubmit"
          >
            Опубликовать
          </button>
          <button
            class="button is-info"
            type="button"
            name="save_blog"
            disabled
          >
            Сохранить как черновик
          </button>
        </div>
      </div>
    </div>
    <div v-if="!$auth.loggedIn" class="warning-overlay">
      <warning
        title="Оповещение"
        body="Для возможности создания блога вам необходимо авторизоваться"
        button="Войти"
        redirect="/login"
      />
    </div>
  </div>
</template>

<script>
import Warning from '@/components/Warning'
import imageField from '@/components/blog/imageField'
import textField from '@/components/blog/textField'
import videoField from '@/components/blog/videoField'
import { reportEditor } from '~/assets/descriptions'

export default {
  components: {
    Warning,
    textField,
    imageField,
    videoField,
  },
  data() {
    return {
      report: {
        title: '',
        date_start: null,
        date_end: null,
        fishing: '',
        category: '',
        tags: '',
        areal: '',
        city: '',
        remark: '',
      },
      buttons: [
        {
          type: 'Текст',
          field: 'textField',
        },
        {
          type: 'Изображение',
          field: 'imageField',
        },
        {
          type: 'Видео',
          field: 'videoField',
        },
      ],
      articles: ['textField'],
      report_body: [],
      report_title: null,
      report_category: 'Блоги',
      report_tags: ['Текст'],
      options: ['Видео', 'Картинки', 'Текст'],
      errorTags: '',
    }
  },
  head() {
    return {
      title: reportEditor.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: reportEditor.description,
        },
      ],
    }
  },
  methods: {
    removeElement(id) {
      this.report_body = this.report_body.filter((item) => {
        return item.name !== id
      })
    },
    fillBlog(val) {
      const block = this.report_body.find((item) => item.name === val.name)
      if (block) {
        block.body = val.body
      } else {
        this.report_body.push(val)
      }
    },
    error(text) {
      this.$buefy.toast.open({
        duration: 5000,
        message: text,
        type: 'is-danger',
      })
    },
    addTag(newTag) {
      this.options.push(newTag)
      this.report_tags.push(newTag)
    },
    clearError() {
      this.errorTags = null
    },
    convertBody() {
      return JSON.stringify({
        blocks: [this.report_body],
      })
    },
    addBlock(field) {
      this.articles.push(field)
    },
    async onSubmit() {
      try {
        if (!this.report.title) return this.error('Нужно заполнить поля')

        const tags = JSON.stringify(this.report_tags)

        const report = {
          ...this.report,
          date_start: this.report.date_start.toISOString(),
          date_end: this.report.date_end.toISOString(),
          category: 'хз',
          tags,
        }
        console.log(report)
        const response = await this.$axios.$post('/report/', report)
        console.log('response = ', response)
        this.$router.push({
          name: 'reports -slug',
          params: { slug: response.slug },
        })
      } catch (data) {
        // this.report = {
        //   ...this.report,
        //   date_start: null,
        //   date_end: null,
        // }
        if (data.response.data && data.response.data.fishing) {
          this.error('Поле fishing пустое')
        }
        if (data.response.data && data.response.data.areal) {
          this.error('Поле регион пустое')
        }
        if (data.response.data && data.response.data.city) {
          this.error('Поле города пустое')
        }
        if (data.response.data && data.response.data.remark) {
          this.error('Поле remark пустое')
        }
        if (data.response.data && data.response.data.tags) {
          this.errorTags = 'Слишком много тэгов'
        }
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.report-section {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  margin-bottom: 0;
  section {
    width: 100%;
    margin-bottom: 10px;
    &:nth-child(3n) {
      margin-right: 0;
    }
    @media screen and (min-width: 450px) {
      width: 50%;
      &:not(:nth-child(2n)) {
        width: calc(50% - 10px);
        margin-right: 10px;
      }
    }
  }
}
.tile.is-parent {
  background-color: #f6f6f6;
}
.is-vertical.box {
  @media screen and (max-width: 450px) {
    .buttons {
      justify-content: space-around;
      .button {
        white-space: initial;
        padding: 10px 15px;
        font-size: 15px;
        height: 100%;
      }
    }
  }
  & > div:not(.report-section) {
    margin-bottom: 10px;
  }
  .column {
    padding: 0;
    margin: 0;
    &:not(:last-child) {
      margin-right: 10px;
    }
    @media screen and (max-width: 450px) {
      margin-bottom: 10px;

      &:not(:last-child) {
        margin-right: 0;
      }
    }
  }
  .columns {
    margin: 0;
  }
}
@media screen and (max-width: 450px) {
  .title {
    padding: 15px;
    text-align: center;
    margin: 0;
  }
}
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css" scoped></style>
