<template>
        <div class="card">
            <h5 class="card-header">{{title}}</h5>
            <div class="card-body">
                <p class="card-text">{{body}}</p>
                <router-link :to="redirect" class="button button-gray-outline">{{button}}</router-link>
            </div>
        </div>
</template>

<script>
    export default {
        name: "Warning",
        props:['title', 'body','button', 'redirect']
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
