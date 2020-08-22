<template>
  <div class="card">
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <div class="flex">
            <div class="is-flex">
              <p class="title is-4">
                <b-skeleton width="150px" :animated="animated"></b-skeleton>
              </p>
            </div>
          </div>
        </div>
        <div class="media-right"></div>
      </div>
      <div class="media">
        <div class="media-content">
          <p class="title">
            <b-skeleton width="250px" :animated="animated"></b-skeleton>
          </p>
        </div>
      </div>
      <div class="content">
        <b-skeleton height="80px"></b-skeleton>
      </div>
      <div class="media">
        <div class="columns">
          <div class="column">
            <b-skeleton width="150px" :animated="animated"></b-skeleton>
          </div>
          <div class="column">
            <b-skeleton width="150px" :animated="animated"></b-skeleton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      animated: true,
    }
  },
}
</script>

<style scoped lang="scss">
.blog-category {
  background-color: #1e347b;
  font-size: 45px;
}
.image_container {
  padding: 20px 0;
}
.media {
  align-items: center;
  .title {
    color: #adadad;
    font-weight: 300;
    @media screen and (max-width: 450px) {
      font-size: 20px;
    }
  }
}
.like {
  display: flex;
  flex-flow: column;
}
.flex {
  display: flex;
  align-items: center;
  @media screen and (max-width: 450px) {
    flex-flow: column;
    align-items: flex-start;
    figure {
      margin: 0;
    }
  }
  figure {
    margin: 0 20px;
  }
}
.card-footer {
  padding-top: 1rem;
}
</style>
