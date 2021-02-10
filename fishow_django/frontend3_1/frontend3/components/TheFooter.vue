<template>
  <footer class="footer container">
    <div class="columns">
      <div class="column is-border-bottom">
        <div class="columns">
          <div class="column">
            <div>Статистика по регионам</div>
            <div>Водоемы</div>
            <div>Список рыб</div>
            <div>Туристические базы</div>
          </div>
          <div class="column">
            <div>Мы в социальных сетях</div>
            <div class="icons"></div>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <div>FAQ</div>
            <div>Политика конфиденциальности</div>
            <div>Правила сайта</div>
          </div>
        </div>
        <div class="columns">
          <div class="column">© 2020 Информационный портал fishow.ru</div>
        </div>
      </div>
      <div class="column">
        <div class="column-title">Форма обратной связи</div>
        <div class="form-body">
          <b-field label="Сообщение" :label-position="labelPosition">
            <b-input
              v-model="userMessage"
              maxlength="200"
              type="textarea"
            ></b-input>
          </b-field>
          <b-field label="Почта" :label-position="labelPosition">
            <b-input v-model="userEmail" type="email" maxlength="30"> </b-input>
          </b-field>
          <b-field grouped label="Имя" :label-position="labelPosition">
            <b-input v-model="userName"></b-input>
            <p class="control">
              <b-button @click="sendMessage" class="button is-primary"
                >Отправить</b-button
              >
            </p>
          </b-field>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
// import Lastblogs from './Home/lastblogs'
export default {
  data() {
    return {
      img: null,
      userMessage: '',
      userName: '',
      userEmail: '',
      labelPosition: 'on-border',
      copyText:
        'Все материалы на сайте представлены исключительно для ознакомления и не могут быть использованы в коммерческих целях. Создатели сайта не несут ответственности за собранные здесь материалы. Все авторские права принадлежат их владельцам.',
    }
  },
  mounted() {
    // this.$axios.get('media/586132_gallery.world_ByBDS4T.jpg').then((res) => {
    //   this.img = res.responce
    //   console.log(res.data)
    // })
  },
  methods: {
    sendMessage() {
      try {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Сообщение успешно отправлено!',
          type: 'is-success',
        })
      } catch (e) {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Произошла ошибка при отправке сообщения.',
          type: 'is-danger',
        })
      }
      this.userName = ''
      this.userEmail = ''
      this.userMessage = ''
    },
  },
}
</script>

<style lang="scss" scoped>
footer {
  width: 100%;
}
.is-border-bottom {
  & > div:not(:last-child) {
    border-bottom: 1px solid #2c313647;
  }
}
.column-title {
  margin-bottom: 20px;
}
</style>
