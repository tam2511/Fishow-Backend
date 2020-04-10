<template>
    <section class="section section-variant-1 bg-gray-100">
        <div class="container container__small" :style="maxWidth">
<!--            <div v-if="getStep < 3" class="select-predict">-->
            <div v-if="getStep < 3" class="select-predict">
                <el-steps :active="getStep" finish-status="success">
                    <el-step title="Область"></el-step>
                    <el-step title="Населенный пункт"></el-step>
                    <el-step title="Рыба"></el-step>
                </el-steps>
                <h2>{{ getOblast}}</h2>
                <!--                <el-cascader @change="handleChange" v-model="value" :options="options" placeholder="Ваш выбор" clearable></el-cascader>-->

                <div v-if="getStep === 0">
                    <el-select v-model="value" placeholder="Select" >
                        <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div v-else-if="getStep === 1">
                    <el-select v-model="value2" placeholder="Select" >
                        <el-option
                                v-for="item in options2"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div v-else-if="getStep === 2">
                    <el-select v-model="value3" placeholder="Select" >
                        <el-option
                                v-for="item in options3"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div class="predict_footer">
                    <el-button @click="back">Назад</el-button>
                    <el-button style="margin-top: 12px;" @click="next">Next step</el-button>
                </div>

            </div>
            <div v-else class="predict" v-loading="loading">
                <h4>Россия / Москва </h4>
                <h3>Прогноз на близжайшие 10 дней </h3>
                <el-tabs v-model="activeName">
                    <el-tab-pane v-for="day in days" :key="day.id" :label="day.name" :name="day.label">
                        <column/>
                    </el-tab-pane>
                </el-tabs>
                <div class="predict_footer">
                    <el-button @click="back">Назад</el-button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import Column from "../components/predictPage/column";
    export default {
        name: "PredictPage",
        components: {Column},
        data() {
            return {
                days: [
                    {
                        name : 'Понедельник',
                        label: 'first'
                    },{
                        name : 'Вторник',
                        label: 'first2'
                    },{
                        name : 'Среда',
                        label: 'first3'
                    },{
                        name : 'Четверг',
                        label: 'first4'
                    },{
                        name : 'Пятница',
                        label: 'first5'
                    },{
                        name : 'Суббота',
                        label: 'first6'
                    },{
                        name : 'Воскресенье',
                        label: 'first7'
                    }],
                result: '',
                options: [
                    {
                        value: 'мо',
                        label: 'Московская область',
                    },
                    {
                        value: 'лен обл',
                        label: 'Ленинградская обл',
                        children: [
                            {
                                value: 'СПБ',
                                label: 'Санкт-Петербург',
                                children: [
                                    {
                                        value: 'судак',
                                        label: 'Судак'
                                    }, {
                                        value: 'щука',
                                        label: 'Щука'
                                    }
                                ]
                            },
                            {
                                value: 'Светогорск',
                                label: 'Светогорск',
                                children: [
                                    {
                                        value: 'судак',
                                        label: 'Судак'
                                    }, {
                                        value: 'щука',
                                        label: 'Щука'
                                    }
                                ]
                            }]
                    }],
                options2: [
                    {
                        value: 'москва',
                        label: 'Москва',
                        children: [
                            {
                                value: 'судак',
                                label: 'Судак'
                            }, {
                                value: 'щука',
                                label: 'Щука'
                            }
                        ]
                    }, {
                        value: 'Балашиха',
                        label: 'Балашиха',
                    }],
                options3: [
                    {
                        value: 'судак',
                        label: 'Судак'
                    }, {
                        value: 'щука',
                        label: 'Щука'
                    }
                ],
                pogoda: [
                    {
                        label: 'Скорость ветра: ',
                        value:'24 km/h'
                    },
                    {
                        label: 'Temperature: ',
                        value: '7 °C'
                    },
                    {
                        label: 'Влажность: ',
                        value: '87%'
                    }
                ],
                activeName: 'first',
                active: 0,
                value: '',
                value2: '',
                value3:'',
                loading: true
            }
        },
        computed: {
            getStep() {
                let value = 0
                console.log(this.value)
                if (this.value !== '') value = 1
                if (this.value2 !== '') value = 2
                if (this.value3 !== '') {
                    this.loadingfunc();
                    value = 3
                }
                return value
            },
            getOblast() {
                return this.result[0];
            },
            getCity() {
                return this.result[1];
            },
            getFish() {
                return this.result[this.result.length - 1];
            },
            maxWidth() {
                return this.getStep <= 2 ? 'max-width: 500px' : 'max-width: 100%'
            }
        },
        methods: {
            next() {
                this.getStep = 3
                console.log('this.active = ', this.active);
                if (this.active++ > 2) this.active = 0;
                this.loadingfunc()
            },
            back() {
                this.loading = true
                if (this.active > 0) {
                    this.active -= 1
                }

                this.result = ''
            },
            handleChange(value) {
                console.log(value);
            },
            loadingfunc() {
                setTimeout(() => {
                    this.loading = false;
                }, 2000);
            }
        }

    }
</script>

<style scoped lang="scss">
    .el-cascader {
        margin: 20px 0;
        display: block;
    }
    .el-row {
        margin-bottom: 20px;
        &:last-child {
            margin-bottom: 0;
        }
    }
    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border: 1px solid rgba(0, 0, 0, 0.2);
        min-height: 70px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
    .container__small {
        max-width: 500px;
        padding: 20px;
        border: 1px solid #e1e1e1;
        min-height: 500px;
        background-color: #fff;
        transition: all 0.3s;
        &:hover {
            box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
        }
    }
    .predict,.select-predict {
        position: relative;
        min-height: 458px;
    }
    .predict_footer {
        position: absolute;
        bottom: 0;
        right: 0;
    }
    .el-select {
        display: block;
        padding: 20px 0;
    }
</style>