<template>
  <div class="block-player-info">
    <h4>Настройки</h4>
    <div>
      <label class="typo__label">Выберите тему:</label>
      <multiselect
        v-model="value"
        track-by="label"
        label="label"
        :options="options"
        :searchable="false"
        :close-on-select="true"
        :show-labels="false"
        placeholder="Pick a value"
        @input="setTheme"
      ></multiselect>
      {{ value.value }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      settingsActive: false,
      options: [
        {
          value: 'theme_color_fishow_default',
          label: 'Основная',
        },
        {
          value: 'theme_color_fishow_esoteric',
          label: 'Темная',
        },
        {
          value: 'theme_color_fishow_underwater',
          label: 'Под водой',
        },
      ],
      optionsCategory: ['Стандартная', 'Темная', 'Синяя'],
      value: '',
    }
  },
  methods: {
    setTheme() {
      if (this.value && this.value !== '') {
        console.log('set thheme = ', this.value.value)
        document.getElementById('app').className = 'theme'
        document.getElementById('app').classList.add(this.value.value)
        localStorage.setItem('theme', this.value.value)
      }
    },
  },
}
</script>

<style scoped></style>
