<template>
  <div class="columns uv-table">
    <div class="column" v-for="item in messages" :key="item.icons">
      <div class="icons">
        <icon-protection
          v-for="icons in item.icons"
          :key="icons"
          :value="icons"
        />
      </div>

      <div class="message">{{ item.message }}</div>
      <div class="status">{{ item.status }}</div>
    </div>
  </div>
</template>

<script>
import IconProtection from '~/components/predictPage/Results/UVindex/message/icon-protection'
export default {
  components: { IconProtection },
  data() {
    return {
      messages: [
        {
          icons: ['1-2'],
          message: 'no protection',
          status: 'You can safely stay outide without sun protection measures',
        },
        {
          icons: ['3-5', '6-7'],
          message: 'protection required',
          status: 'You can safely stay outide without sun protection measures',
        },
        {
          icons: ['8-10', '11+'],
          message: 'extra protection',
          status: 'You can safely stay outide without sun protection measures',
        },
      ],
    }
  },
}
</script>

<style scoped>
.column {
  text-align: center;
}
.message {
  padding: 1rem 1.5rem;
  text-transform: uppercase;
  color: #fff;
  background-color: #617e8c;
  font-weight: 700;
}
.uv-table {
  padding-top: 30px;
}
.icons {
  display: flex;
  padding-bottom: 6px;
  justify-content: center;
}
</style>
