import datetime


class UVIndexTextGenerator:

    @staticmethod
    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: sorted([(_.uv_index, _.time) for _ in data if
                                              _.date == observe_date and _.fish == fish], key=lambda x: x[1]) for
                        observe_date in observe_dates}
        # uv_index_0 = [filtred_data[d][0][0] for d in filtred_data]
        # uv_index_3 = [filtred_data[d][1][0] for d in filtred_data]
        uv_index_6 = [filtred_data[d][2][0] for d in filtred_data]
        uv_index_9 = [filtred_data[d][3][0] for d in filtred_data]
        uv_index_12 = [filtred_data[d][4][0] for d in filtred_data]
        uv_index_15 = [filtred_data[d][5][0] for d in filtred_data]
        uv_index_18 = [filtred_data[d][6][0] for d in filtred_data]
        uv_index_21 = [filtred_data[d][7][0] for d in filtred_data]
        return {6: uv_index_6, 9: uv_index_9, 12: uv_index_12, 15: uv_index_15,
                18: uv_index_18, 21: uv_index_21}
