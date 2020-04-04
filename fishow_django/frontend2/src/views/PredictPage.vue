<template>
    <section class="section section-variant-1 bg-gray-100">
        <div class="container">
            <div class="row row-50">
                <el-cascader v-model="value" :options="options" placeholder="Ваш выбор" clearable></el-cascader>
            </div>
            <div class="row row-50">
                <code>{{ value  }}</code>
            </div>
            <div class="row row-50 ">
                <ul class="list list-group">
                    <li>Область: {{ getOblast }}</li>
                    <li>Город: {{ getCity}}</li>
                    <li>Выбрана рыба: {{ getFish }}</li>
                </ul>
            </div>
            <el-row :gutter="20" style="margin-top: 30px">
                <el-col :span="6" v-for="card in pogoda" :key="card">
                    <div class="grid-content bg-purple">
                        <el-card class="box-card">
                            <div class="text item">
                                {{card.label + card.value }}
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>
        </div>

    </section>
</template>

<script>
    export default {
        name: "PredictPage",

        data() {
            return {
                value: '',
                options: [
                    {
                        value: 'мо',
                        label: 'Московская область',
                        children: [
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
                // riba: {'prob': 0.8,
                //     'importance_features':
                //         {'names': [('gust', 1, 3),
                //                 ('пасмурно', 0, 0),
                //                 ('gust', 0, 0),
                //                 ('sub_temperature', 2, 0)
                //             ],
                //             'values': [18.0, 1.0, 6.0, -2.0]
                //         }
                // }
            }
        },
        computed: {
            getOblast() {
                return this.value[0];
            },
            getCity() {
                return this.value[1];
            },
            getFish() {
                return this.value[this.value.length - 1];
            }
        }
    }
</script>

<style scoped lang="scss">
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
        border-radius: 4px;
        min-height: 36px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>