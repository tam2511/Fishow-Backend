<template>
        <div class="card">
            <h5 class="card-header">{{title}}</h5>
            <div class="card-body">
                <p class="card-text">{{body}}</p>
                <button @click="setShow" class="button button-gray-outline">{{button}}</button>
            </div>
        </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    export default {
        name: "Warning",
        props:['title', 'body','button', 'redirect'],
        computed: {
            ...mapState('login', ['show'])
        },
        methods: {
            ...mapActions('login', ['setShow'])
        }
    }
</script>

<style scoped>
    .card {
        margin: auto;
        max-width: 300px;
        background: var(--background-color-primary);
    }
    .card-text {
        color: var(--color-typo-primary)
    }
</style>
