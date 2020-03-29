<template>
    <div class="player-info-corporate">
        <div class="player-info-figure">
            <div class="block-number"><span>11</span></div>
            <div class="player-img"><img src="/static/assets/images/roster-player-2-368x286.jpg" alt="" width="368" height="286"/>
            </div>
        </div>
        <div class="player-info-main">
            <h4 class="player-info-title">{{ userName }}</h4>
            <p class="player-info-subtitle">Forward</p>
            <hr/>
            <div class="player-info-table">
                <div class="table-custom-wrap">
                    <table class="table-custom">
                        <tr>
                            <th>Age</th>
                            <th>20</th>
                            <th>Height</th>
                            <th>5’8”</th>
                        </tr>
                        <tr>
                            <td>Weight</td>
                            <td>176 IBS</td>
                            <td>Total games</td>
                            <td>150</td>
                        </tr>
                    </table>
                </div>
            </div>
            <hr/>
            <div class="player-info-progress">
                <!-- Linear progress bar-->
                <article class="progress-linear progress-bar-modern">
                    <div class="progress-header">
                        <p>Pass Acc</p>
                    </div>
                    <div class="progress-bar-linear-wrap">
                        <div class="progress-bar-linear"></div>
                    </div><span class="progress-value">95</span>
                </article>
                <!-- Linear progress bar-->
                <article class="progress-linear progress-bar-modern">
                    <div class="progress-header">
                        <p>Shots Acc</p>
                    </div>
                    <div class="progress-bar-linear-wrap">
                        <div class="progress-bar-linear"></div>
                    </div><span class="progress-value">70</span>
                </article>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserMain",
        data() {
            return {
                userName: null
            }
        },
        methods: {
            getUserName() {
                if (window.localStorage.getItem("username")) {
                    this.userName = window.localStorage.getItem("username");
                }

            }
        },
        created() {
            this.getUserName();
        }
    }
</script>

<style scoped>

</style>