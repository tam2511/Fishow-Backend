<template>
  <div class="media card-footer">
    <div v-if="author" class="is-flex blog-author">
      <figure class="image is-16x16">
        <img
          src="https://bulma.io/images/placeholders/96x96.png"
          alt="Placeholder image"
        />
      </figure>
      <p>{{ author }}</p>
      <time v-if="createdAt" datetime="2016-1-1">{{ createdAt }}</time>
    </div>
    <div>
      <b-field grouped group-multiline>
        <div class="control">
          <b-taglist attached>
            <nuxt-link
              v-if="slugRoute"
              :to="{ name: 'blog-slug', params: { slug: slugRoute } }"
            >
              <b-tag type="is-light">Комментариев</b-tag>
              <b-tag type="is-primary">{{ commentsCount }}</b-tag>
            </nuxt-link>
          </b-taglist>
        </div>
      </b-field>
      <b-tag v-if="category" class="blog-category" type="is-primary">{{
        category
      }}</b-tag>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardFooter',
  props: {
    slugRoute: {
      type: String,
      default() {
        return ''
      },
    },
    category: {
      type: String,
      default() {
        return ''
      },
    },
    commentsCount: {
      type: [String, Number],
      default() {
        return ''
      },
    },
    createdAt: {
      type: String,
      default() {
        return ''
      },
    },
    author: {
      type: String,
      default() {
        return ''
      },
    },
  },
}
</script>

<style lang="scss" scoped>
.media.card-footer {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  & > div > * {
    margin: 0 10px;
  }
  padding-top: 10px;
  .field.is-grouped.is-grouped-multiline > .control:last-child {
    margin: 0;
  }
  & > * {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: space-around;
  }
}
</style>
