<template>
  <div class="columns uv-table">
    <div v-for="item in messages" :key="item.icons[0]" class="column">
      <div class="icons">
        <icon-protection
          v-for="icons in item.icons"
          :key="icons.id"
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
          message: 'слабая активность',
          status: 'Вы можете спокойно оставаться на улице без средств защиты от солнца',
        },
        {
          icons: ['3-5', '6-7'],
          message: 'средняя активность',
          status: 'Нанесите солнцезащитный крем SPF 30+ и оставайтесь в тени около полудня, когда солнце наиболее опасно.',
        },
        {
          icons: ['8-10', '11+'],
          message: 'сильная активность',
          status: 'Наденьте футболку, кепку и очки, нанесите солнцезащитный крем SPF 50+, оставайтесь в тени как можно дольше и не выходите на улицу в полдень.',
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
