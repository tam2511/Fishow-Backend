'''
Тестирование генерации текста на основе временных порогов
'''

from helper import influence_text_generate, influence_tendays_text_generate


class InfluenceTextGenerator:
    influence_time1 = [(0, 0)]
    influence_time2 = [(0, 6)]
    influence_time3 = [(0, 12)]
    influence_time4 = [(0, 21)]
    influence_time5 = [(0, 6), (0, 21)]
    influence_time6 = [(0, 3), (0, 12), (0, 18)]
    influence_time7 = [(0, 0), (0, 9), (0, 15), (0, 18)]
    influence_time8 = [(1, 18)]
    influence_time9 = [(0, 0), (0, 9), (0, 15), (0, 18), (4, 3)]

    @staticmethod
    def test1():
        expected_value = 'сегодня ночью'
        assert influence_text_generate(InfluenceTextGenerator.influence_time1) == expected_value

    @staticmethod
    def test2():
        expected_value = 'сегодня утром'
        assert influence_text_generate(InfluenceTextGenerator.influence_time2) == expected_value

    @staticmethod
    def test3():
        expected_value = 'сегодня днем'
        assert influence_text_generate(InfluenceTextGenerator.influence_time3) == expected_value

    @staticmethod
    def test4():
        expected_value = 'сегодня вечером'
        assert influence_text_generate(InfluenceTextGenerator.influence_time4) == expected_value

    @staticmethod
    def test5():
        expected_value = 'сегодня утром и вечером'
        assert influence_text_generate(InfluenceTextGenerator.influence_time5) == expected_value

    @staticmethod
    def test6():
        expected_value = 'сегодня днем, вечером и ночью'
        assert influence_text_generate(InfluenceTextGenerator.influence_time6) == expected_value

    @staticmethod
    def test7():
        expected_value = 'сегодня утром, днем, вечером и ночью'
        assert influence_text_generate(InfluenceTextGenerator.influence_time7) == expected_value

    @staticmethod
    def test8():
        expected_value = 'в ближайшие трое суток'
        assert influence_text_generate(InfluenceTextGenerator.influence_time8) == expected_value

    @staticmethod
    def test9():
        expected_value = 'сегодня утром, днем, вечером, ночью и в ближайшие трое суток'
        assert influence_text_generate(InfluenceTextGenerator.influence_time9) == expected_value


InfluenceTextGenerator.test1()
InfluenceTextGenerator.test2()
InfluenceTextGenerator.test3()
InfluenceTextGenerator.test4()
InfluenceTextGenerator.test5()
InfluenceTextGenerator.test6()
InfluenceTextGenerator.test7()
InfluenceTextGenerator.test8()
InfluenceTextGenerator.test9()
