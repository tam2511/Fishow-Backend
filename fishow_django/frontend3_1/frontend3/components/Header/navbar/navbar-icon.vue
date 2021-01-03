<template>
  <div>
    <svg
      v-if="type === 'Close'"
      width="36"
      height="36"
      viewBox="0 0 36 36"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="close_24px">
        <path
          id="icon/navigation/close_24px"
          d="M28.5 9.615L26.385 7.5L18 15.885L9.615 7.5L7.5 9.615L15.885 18L7.5 26.385L9.615 28.5L18 20.115L26.385 28.5L28.5 26.385L20.115 18L28.5 9.615Z"
          :fill="color"
        />
      </g>
    </svg>
    <svg
      v-if="type === 'Home'"
      width="36"
      height="36"
      viewBox="0 0 36 36"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="home_24px">
        <path
          id="icon/action/home_24px"
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M7.5 18.75H3L18 5.25L33 18.75H28.5V30.75H19.5V21.75H16.5V30.75H7.5V18.75ZM25.5 16.035L18 9.285L10.5 16.035V27.75H13.5V18.75H22.5V27.75H25.5V16.035Z"
          :fill="color"
        />
      </g>
    </svg>
    <svg
      v-if="type === 'CreateBlog'"
      width="38"
      height="38"
      viewBox="0 0 38 38"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="add_circle_outline_24px">
        <path
          id="icon/content/add_circle_outline_24px"
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M19 3.16666C10.26 3.16666 3.16669 10.26 3.16669 19C3.16669 27.74 10.26 34.8333 19 34.8333C27.74 34.8333 34.8334 27.74 34.8334 19C34.8334 10.26 27.74 3.16666 19 3.16666ZM17.4167 11.0833V17.4167H11.0834V20.5833H17.4167V26.9167H20.5834V20.5833H26.9167V17.4167H20.5834V11.0833H17.4167ZM6.33335 19C6.33335 25.9825 12.0175 31.6667 19 31.6667C25.9825 31.6667 31.6667 25.9825 31.6667 19C31.6667 12.0175 25.9825 6.33332 19 6.33332C12.0175 6.33332 6.33335 12.0175 6.33335 19Z"
          :fill="color"
        />
      </g>
    </svg>
    <svg
      v-if="type === 'Person'"
      width="36"
      height="36"
      viewBox="0 0 36 36"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="person_24px">
        <path
          id="icon/social/person_24px"
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M16 5.33334C13.0533 5.33334 10.6666 7.72001 10.6666 10.6667C10.6666 13.6133 13.0533 16 16 16C18.9466 16 21.3333 13.6133 21.3333 10.6667C21.3333 7.72001 18.9466 5.33334 16 5.33334ZM18.6666 10.6667C18.6666 9.20001 17.4666 8.00001 16 8.00001C14.5333 8.00001 13.3333 9.20001 13.3333 10.6667C13.3333 12.1333 14.5333 13.3333 16 13.3333C17.4666 13.3333 18.6666 12.1333 18.6666 10.6667ZM24 24C23.7333 23.0533 19.6 21.3333 16 21.3333C12.4133 21.3333 8.30665 23.04 7.99998 24H24ZM5.33331 24C5.33331 20.4533 12.44 18.6667 16 18.6667C19.56 18.6667 26.6666 20.4533 26.6666 24V26.6667H5.33331V24Z"
          :fill="color"
        />
      </g>
    </svg>
    <svg
      v-if="type === 'Terrain'"
      width="38"
      height="38"
      viewBox="0 0 38 38"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="terrain_24px">
        <path
          id="icon/maps/terrain_24px"
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M15.485 18.4142L22.1666 9.5L36.4166 28.5H1.58331L10.3391 16.8308L16.6883 25.3333H30.0833L22.1666 14.7725L17.4641 21.0583L15.485 18.4142ZM10.3233 22.1192L7.91665 25.3333H12.73L10.3233 22.1192Z"
          :fill="color"
        />
      </g>
    </svg>
    <svg
      v-if="type === 'hot'"
      width="36"
      height="36"
      viewBox="0 0 36 36"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g id="whatshot_24px">
        <path
          id="icon/social/whatshot_24px"
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M20.25 2.0025C20.25 2.0025 21.36 5.9775 21.36 9.2025C21.36 12.2925 19.335 14.7975 16.245 14.7975C13.14 14.7975 10.8 12.2925 10.8 9.2025L10.845 8.6625C7.815 12.2625 6 16.9275 6 21.9975C6 28.6275 11.37 33.9975 18 33.9975C24.63 33.9975 30 28.6275 30 21.9975C30 13.9125 26.115 6.6975 20.25 2.0025ZM17.355 20.7375C15.315 21.1575 14.1 22.4775 14.1 24.3525C14.1 26.3625 15.765 27.9825 17.835 27.9825C20.91 27.9825 23.4 25.4925 23.4 22.4175C23.4 20.8125 23.175 19.2375 22.71 17.7375C21.525 19.3425 19.41 20.3175 17.355 20.7375ZM9 21.9975C9 26.9625 13.035 30.9975 18 30.9975C22.965 30.9975 27 26.9625 27 21.9975C27 18.1575 26.01 14.4525 24.165 11.1525C23.37 15.0525 20.235 17.7975 16.245 17.7975C13.905 17.7975 11.805 16.8675 10.29 15.3525C9.45 17.4375 9 19.7025 9 21.9975Z"
          :fill="color"
        />
      </g>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'Blogs',
    },
    color: {
      type: String,
      default: '#BDBDBD',
    },
  },
}
</script>

<style scoped>
path {
  transition: 0.3s;
}
</style>
