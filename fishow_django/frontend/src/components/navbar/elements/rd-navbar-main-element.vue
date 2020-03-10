<template>
    <div class="rd-navbar-main-element">
        <ul class="list-inline list-inline-bordered">
            <li class="rd-navbar-search-wrap">
                <!-- RD Navbar Search-->
                <div class="rd-navbar-search">
                    <button
                            class="rd-navbar-search-toggle"
                            data-rd-navbar-toggle=".rd-navbar-search"
                    >
                        <span></span>
                    </button>
                    <form
                            class="rd-search"
                            action=""
                            data-search-live="rd-search-results-live"
                            method="GET"
                    >
                        <div class="form-wrap">
                            <label
                                    class="form-label"
                                    for="rd-navbar-search-form-input"
                            >Enter your search request here...</label
                            >
                            <input
                                    class="rd-navbar-search-form-input form-input"
                                    id="rd-navbar-search-form-input"
                                    type="text"
                                    name="s"
                                    autocomplete="off"
                            />
                            <div
                                    class="rd-search-results-live"
                                    id="rd-search-results-live"
                            ></div>
                        </div>
                        <button
                                class="rd-search-form-submit fl-budicons-launch-search81"
                                type="submit"
                        ></button>
                    </form>
                </div>
            </li>
            <li>
                <a
                        class="link link-icon link-icon-left link-classic"
                        href=""
                >Вход/Регистрация
                    <span class="icon fl-bigmug-line-login12"></span
                    ></a>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "rd-navbar-main-element"
    }
</script>

<style scoped lang="scss">

</style>