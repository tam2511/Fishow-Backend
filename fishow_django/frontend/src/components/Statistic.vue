<template>
    <div class="table-custom-responsive">
        <table
                class="table-custom table-custom-bordered table-team-statistic"
        >
            <tbody>
            <tr>
                <td>
                    <p class="team-statistic-counter">{{ counterBlogs }}</p>
                    <p class="team-statistic-title">Всего блогов</p>
                </td>
                <td>
                    <p class="team-statistic-counter">0</p>
                    <p class="team-statistic-title">Rebounds Per Game</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p class="team-statistic-counter">0</p>
                    <p class="team-statistic-title">Assists Per Game</p>
                </td>
                <td>
                    <p class="team-statistic-counter">0</p>
                    <p class="team-statistic-title">Points Allowed</p>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "Statistic",
        data() {
            return {
                counterBlogs: null
            }

        },
        methods: {
            getBlogData() {
                let endpoint = `/api/blogs/`;
                apiService(endpoint).then(data => {
                    console.log(data);
                    this.counterBlogs = data.count;
                })
            },
        },
        created() {
            this.getBlogData();
        }
    }
</script>

<style scoped>

</style>