<template>
    <el-row :gutter="20">
        <one-colum v-for="n in 4" :key="n"/>
    </el-row>
</template>

<script>
    import OneColum from "./oneColumn";
    export default {
        name: "colum",
        data() {
          return {

          }
        },
        components: {OneColum}
    }
</script>

<style>

</style>