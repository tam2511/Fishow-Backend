<template>
    <div class="table-custom-responsive">
        <table class="table-custom table-standings table-classic">
            <thead>
            <tr>
                <th colspan="2">Пользователи</th>
                <th>Сообщ.</th>
                <th>Блогов</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="n in 10">
                <td><span>{{ n }}</span></td>
                <td class="team-inline">
                    <div class="team-figure">
                        <img
                                src=""
                                alt=""
                                width="42"
                                height="26"
                        />
                    </div>
                    <div class="team-title">
                        <div class="team-name">Имя</div>
                        <div class="team-country">Фамилия</div>
                    </div>
                </td>
                <td>153</td>
                <td>30</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: "UserRate"
    }
</script>

<style scoped>

</style>