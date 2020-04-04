/<template>
    <div class="rd-navbar-main rd-navbar-dark">
        <div class="rd-navbar-main-container container">
            <!-- RD Navbar Brand-->
            <div class="rd-navbar-brand">
                <router-link class="brand fishow_logo" to="/">Fishow</router-link>
            </div>
            <!-- RD Navbar Nav-->
            <ul class="rd-navbar-nav">
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/">Главная</router-link>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/predict-page">Прогноз</router-link>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/gallery">Галерея</router-link>
                    <!-- RD Navbar Dropdown-->
                    <ul class="rd-menu rd-navbar-dropdown">
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/fotoalbum">Фотоальбом</router-link>
                        </li>
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/videoalbum">Видеоальбом</router-link>
                        </li>
                    </ul>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/news">Новости</router-link>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/article">Статьи</router-link>
                    <!-- RD Navbar Dropdown-->
                    <ul class="rd-menu rd-navbar-dropdown">
                        <li class="rd-dropdown-item"><router-link class="rd-dropdown-link" to="">Истории</router-link>
                        </li>
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/empty">Блоги</router-link>
                        </li>
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/empty2">Отчеты</router-link>
                        </li>
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/blog-editor">Написать Блог</router-link>
                        </li>
                        <li class="rd-dropdown-item">
                            <router-link class="rd-dropdown-link" to="/empty3">Написать Статью</router-link>
                        </li>
                    </ul>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/wiki">Вики</router-link>
                </li>
                <li class="rd-nav-item">
                    <router-link class="rd-nav-link" to="/forum">Форум</router-link>
                </li>
            </ul>
            <rd-navbar-main-element/>
        </div>
    </div>
</template>

<script>
import RdNavbarMainElement from './elements/rd-navbar-main-element.vue'
export default {
  name: 'rd-navbar-main',
  components: { RdNavbarMainElement }
}
</script>

<style scoped lang="scss">
    a:active {
        color: #fff;
    }
</style>
