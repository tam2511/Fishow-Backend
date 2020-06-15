<template>
  <div class="card box">
    <b-menu>
      <b-menu-list label="Главная">
        <b-menu-item
          label="Главная странциа"
          icon="home"
          tag="nuxt-link"
          to="/"
        ></b-menu-item>
      </b-menu-list>
      <b-menu-list label="Меню">
        <b-menu-item icon="information-outline" label="Город"></b-menu-item>
        <b-menu-item icon="information-outline" label="Рыба"></b-menu-item>
        <b-menu-item>
          <template slot="label" slot-scope="props">
            Прогноз
            <b-icon
              class="is-pulled-right"
              :icon="props.extended ? 'menu-down' : 'menu-up'"
            >
            </b-icon>
          </template>
          <b-menu-item icon="account" label="Клев"></b-menu-item>
        </b-menu-item>
        <b-menu-item icon="settings" :active="isActive" expanded>
          <template slot="label" slot-scope="props">
            Погода
            <b-icon
              class="is-pulled-right"
              :icon="props.expanded ? 'menu-down' : 'menu-up'"
            ></b-icon>
          </template>
          <b-menu-item icon="account" label="Температура"></b-menu-item>
          <b-menu-item icon="cellphone-link">
            <template slot="label">
              Осадки
            </template>
          </b-menu-item>
        </b-menu-item>
        <b-menu-item icon="account" label="My Account">
          <b-menu-item label="Account data"></b-menu-item>
          <b-menu-item label="Addresses"></b-menu-item>
        </b-menu-item>
      </b-menu-list>
      сть
      <b-menu-list label="Actions">
        <b-menu-item label="Logout"></b-menu-item>
      </b-menu-list>
    </b-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      mini: true,
      isActive: false,
    }
  },
  created() {},
  methods: {},
}
</script>

<style scoped></style>
