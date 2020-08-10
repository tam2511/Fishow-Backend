<template>
  <footer class="footer">
    <div class="content has-text-centered">
      <p>
        {{ copyText }}
        Fishow.ru 2020
        {{ img }}
      </p>
    </div>
  </footer>
</template>

<script>
// import Lastblogs from './Home/lastblogs'
export default {
  data() {
    return {
      img: null,
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
}
</script>

<style scoped>
footer {
  position: relative;
  width: 100%;
}
</style>
