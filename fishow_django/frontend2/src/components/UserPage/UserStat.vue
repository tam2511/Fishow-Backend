<template>
  <div class="col-md-6 col-lg-12">
    <!-- Heading Component-->
    <article class="heading-component">
      <div class="heading-component-inner">
        <h5 class="heading-component-title">Statistics</h5>
        <div class="heading-component-aside">
          <select
            class="select select-minimal"
            data-placeholder="All Competitions"
            data-dropdown-class="select-minimal-dropdown"
            style="min-width: 160px;"
          >
            <option value="all" selected="">All Competitions</option>
            <option value="world">World Champions</option>
          </select>
        </div>
      </div>
    </article>

    <!-- List Statistics-->
    <ul class="list-statictics">
      <li>
        <a href="#">Goals scored</a
        ><span class="list-statictics-counter">50</span>
      </li>
      <li>
        <a href="#">Shots</a><span class="list-statictics-counter">25</span>
      </li>
      <li>
        <a href="#">Shots on target</a
        ><span class="list-statictics-counter">10</span>
      </li>
      <li>
        <a href="#">Assists</a><span class="list-statictics-counter">80</span>
      </li>
      <li>
        <a href="#">Key Passes</a
        ><span class="list-statictics-counter">50</span>
      </li>
      <li>
        <a href="#">Dribbles</a><span class="list-statictics-counter">25</span>
      </li>
      <li>
        <a href="#">Fouls</a><span class="list-statictics-counter">10</span>
      </li>
      <li>
        <a href="#">Minutes played</a
        ><span class="list-statictics-counter">500</span>
      </li>
      <li>
        <a href="#">Yellow Cards</a
        ><span class="list-statictics-counter">25</span>
      </li>
      <li>
        <a href="#">Red Cards</a><span class="list-statictics-counter">02</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'UserStat',
}
</script>

<style scoped></style>
