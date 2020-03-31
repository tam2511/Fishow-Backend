<template>
    <article class="game-result game-result-classic">
        <div class="game-result-main">
            <div class="game-result-team game-result-team-first">
                <div style="font-size: 35px">2%</div>
                <div class="game-result-team-name">Прогноз клева</div>
            </div>
            <div class="game-result-team game-result-team-second">
                <span>Скорость ветра: 10м/с</span>
                <span>Темп. воздуха: -16 C</span>
                <div class="game-result-team-name">Погодные условия</div>
            </div>
        </div>
        <div class="game-result-footer">
            <ul class="game-result-details" style="font-weight: 800">
                <li>Сом</li>
                <li>р.Кама</li>
                <li><time datetime="2018-04-14">16-02-2020</time></li>
            </ul>
        </div>
    </article>
</template>

<script>
export default {
  name: 'MiniPrognos'
}
</script>

<style scoped>

</style>
