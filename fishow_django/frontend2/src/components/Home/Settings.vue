<template>
    <div class="settings">
        <button class="settings-btn" type="button" tabindex="-1" @click="activateBtn">Н</button>
        <div :class="{
              'settings-container settings-show': settingsActive,
              'settings-container': !settingsActive
            }">
            <el-select v-model="value" placeholder="Select" :change="setTheme()">
                <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Settings",
        data() {
            return {
                settingsActive: false,
                options: [{
                    value: 'theme_color_fishow_default',
                    label: 'default'
                }, {
                    value: 'theme_color_fishow_dark',
                    label: 'dark'
                }, {
                    value: 'theme_color_fishow_esoteric',
                    label: 'vip'
                }],
                value: ''
            }
        },
        methods: {
            setTheme() {
                console.log('this.theme = ', this.value)
                if (this.value && this.value !== '') {
                    document.getElementById('app').className = 'theme'
                    document.getElementById('app').classList.add(this.value)
                    localStorage.setItem('theme', this.value)
                }

            },
            activateBtn() {
                if (this.settingsActive) {
                    this.settingsActive = false
                } else this.settingsActive = true
                console.log('click', this.settingsActive);
            }
        }
    }
</script>

<style scoped>
    .settings {
        position: fixed;
        top: 65px;
        left: 3px;
        z-index: 100;
    }
    .settings-container {
        transition-duration: 0.3s;
        opacity: 0;
        width: 0;
    }
    .settings-show {
        opacity: 1;
        width: auto;
    }
    .settings-btn {
        color: var(--color-typo-brand);
        border-radius: 2px;
        background-color: var(--background-color-invert);
        border: var(--background-color-border);
    }
</style>