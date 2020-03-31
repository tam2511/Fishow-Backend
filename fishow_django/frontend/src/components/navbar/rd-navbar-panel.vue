<template>
    <div class="rd-navbar-panel">
        <!-- RD Navbar Toggle-->
        <button
                class="rd-navbar-toggle"
                data-rd-navbar-toggle=".rd-navbar-main">
            <span></span>
        </button>
        <!-- RD Navbar Panellist-->
        <div class="rd-navbar-panel-inner container">
            <div class="rd-navbar-panel-item rd-navbar-panel-list">
                <ul class="list-inline list-inline-middle list-inline-sm">
                    <li class="rd-mail-link">
                        <div class="unit unit-horizontal unit-spacing-xs">
                            <div class="unit-left">
                        <span
                                class="icon icon-secondary fl-bigmug-line-email64"
                        ></span>
                            </div>
                            <div class="unit-body">
                                <a class="link-light" href="mailto:#"
                                >info@demolink.org</a
                                >
                            </div>
                        </div>
                    </li>
                    <li>
                        <ul class="list-inline list-inline-xs">
                            <li>
                                <a class="icon icon-xs icon-light fa fa-facebook" href="#"></a>
                            </li>
                            <li>
                                <a class="icon icon-xs icon-light fa fa-twitter" href="#"></a>
                            </li>
                            <li>
                                <a class="icon icon-xs icon-light fa fa-google-plus" href="#"></a>
                            </li>
                            <li>
                                <a class="icon icon-xs icon-light fa fa-instagram" href="#"></a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div
                    class="rd-navbar-collapse-toggle rd-navbar-fixed-element-1"
                    data-rd-navbar-toggle=".rd-navbar-collapse">
                <span></span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'rd-navbar-panel'
}
</script>

<style>

</style>
