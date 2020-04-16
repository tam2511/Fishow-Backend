<template>
    <div class="icon-pogoda" :style="{background : 'linear-gradient(0deg, var('+this.color+')'+getRandom15*this.height+'%, rgba(0,212,255,0)'+getRandom15*this.height+'%'}">
        <span :style="{ bottom: getRandom15 / this.marginText + 15 + 'px' }">
            {{ getRandom15 }}
        </span>

    </div>
</template>

<script>
    export default {
        name: "IconPogoda",
        props: {
            maxValue : {
                type: Number,
                required: true,
            },
            minValue : {
                type: Number,
                required: true,
            },
            color : {
                type: String,
                required: true,
            },
            height : {
                type: Number,
                required: true
            },
            marginText : {
                type: Number,
                required: true
            }

        },
        computed: {
            getRandom15() {
                return Math.floor(Math.random() * (this.maxValue - this.minValue) + this.minValue)
            },

        }
    }
</script>

<style scoped lang="scss">

    .icon-pogoda {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: baseline;
        justify-content: center;
        text-align: center;
        position: relative;
        span {
         position: absolute;
        }
    }
</style>