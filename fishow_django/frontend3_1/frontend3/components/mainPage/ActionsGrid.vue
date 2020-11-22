<template>
  <div class="actions-grid">
    <div class="actions-grid__item">
      <div class="grid__item_title">Создать свою статью</div>
      <div class="grid__item_body">
        Опишите свои впечатления о рыбалке и поделитесь опытом!
      </div>
    </div>
    <div class="actions-grid__item">
      <div class="grid__item_title">Отчеты о рыбалке</div>
      <div class="grid__item_body">
        Опишите свои впечатления о рыбалке и поделитесь опытом!
      </div>
    </div>
    <div class="actions-grid__item">
      <div class="grid__item_title">Статьи и блоги других авторов</div>
      <div class="grid__item_body">
        Читайте интересные истории товарищей по рыбалке
      </div>
    </div>
    <div class="actions-grid__item">
      <div class="grid__item_title">База знаний рыбалова</div>
      <div class="grid__item_body">
        Крупнейшее вики рыбаловного сообщества
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActionsGrid',
}
</script>

<style scoped lang="scss">
.actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 15px;
  row-gap: 15px;
  @media screen and (max-width: 768px) {
    grid-template-columns: 1fr;
  }
  &__item {
    min-height: 220px;
    background-image: url('/Rectangle.png');
    background-position: right;
    background-repeat: no-repeat;
    background-size: cover;
    padding: 20px;

    border: 1px solid rgba(206, 209, 213, 0.4);
    box-sizing: border-box;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
    transition: 0.35s;
    cursor: pointer;
    &:hover {
      box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.18);
    }
  }
}
.grid__item_title {
  font-size: 19px;
  line-height: 32px;
  width: 50%;
}
.grid__item_body {
  text-align: left;
  width: 70%;
}
</style>
