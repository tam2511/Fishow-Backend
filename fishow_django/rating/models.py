from django.db import models
from django.conf import settings



class Rating_waterplace(models.Model):
    water_places = models.CharField(max_length=100)
    fish = models.CharField(max_length=100)
    #town = models.ForeignKey(Rating_Region,related_name='town_region')
    rating = models.FloatField(default=0)
    address = models.CharField(max_length=500)
    prices = models.CharField(max_length=500)
    contacts = models.CharField(max_length=500)
    site = models.CharField(max_length=500)
    fishing_frequency = models.CharField(max_length=500)
    last_fishing = models.DateTimeField()
    #water_view
    fishing_average_jan = models.CharField(max_length=500)
    fishing_average_feb = models.CharField(max_length=500)
    fishing_average_mar = models.CharField(max_length=500)
    fishing_average_apr = models.CharField(max_length=500)
    fishing_average_may = models.CharField(max_length=500)
    fishing_average_jun = models.CharField(max_length=500)
    fishing_average_jul = models.CharField(max_length=500)
    fishing_average_aug = models.CharField(max_length=500)
    fishing_average_sep = models.CharField(max_length=500)
    fishing_average_oct = models.CharField(max_length=500)
    fishing_average_nov = models.CharField(max_length=500)
    fishing_average_dec = models.CharField(max_length=500)

#     Название водоема (строка)
#     Ближайшие города к водоему (ManytoMany ForeignKey)
#     Рейтинг водоема (float)
#     Адрес (строка)
#     Цены (строка)
#     Контакты (строка)
#     Сайт водоема (строка)
#     Частота зарыбления (строка)
#     Последнее зарыбление (дата)
#     Отчеты к нему (OnetoMany ForeignKey)
#     Комментарии к нему ?
#     Страница водоема (на нашем сайте) (строка)
#     Средний улов в январе (float)
#     Средний улов в феврале (float)
#     ....
#     Средний улов в декабре (float)
    def __str__(self):
        return self.content

class Rating_region(models.Model):
    region = models.CharField(max_length=100)
    fish = models.CharField(max_length=100)
    #water_places = models.ManyToManyField(models.Rating_waterplace,related_name='water_place')
    fishing_activity_jan = models.CharField(max_length=500)
    fishing_activity_feb = models.CharField(max_length=500)
    fishing_activity_mar = models.CharField(max_length=500)
    fishing_activity_apr = models.CharField(max_length=500)
    fishing_activity_may = models.CharField(max_length=500)
    fishing_activity_jun = models.CharField(max_length=500)
    fishing_activity_jul = models.CharField(max_length=500)
    fishing_activity_aug = models.CharField(max_length=500)
    fishing_activity_sep = models.CharField(max_length=500)
    fishing_activity_oct = models.CharField(max_length=500)
    fishing_activity_nov = models.CharField(max_length=500)
    fishing_activity_dec = models.CharField(max_length=500)
# Название региона (строка)
# Рыба (строка)
# Список водоемов (OnetoMany ForeignKey)
# Активность клева в январе (float)
# ...
# Активность клева в декабре (float)
    def __str__(self):
        return self.content







# class Comment_rating_water(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     body = models.TextField()
#     report = models.ForeignKey(Report,
#                              on_delete=models.CASCADE,
#                              related_name='comments_r')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.CASCADE)
#     votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                     related_name='votesUp_r')
#     votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                     related_name='votesDown_r')
#
#     def __str__(self):
#         return self.author.username
# # Create your models here.