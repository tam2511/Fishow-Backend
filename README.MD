.\env\Scripts\activate

python manage.py runserver

Backend

1. cd fishow_django

2. python -m venv env

3. Activate env

4. pip3 install -r requirements.txt

~ python3 manage.py migrate --run-syncdb

API

127.0.0.1/api/...
https://back.fishow.ru/api/...

1. BLOGS,COMMENTS
Апи по по работе со Статьями

Получить список статей (Method GET)
* blogs/

Получить список статей в которых есть одновременно слово1 и слово2 (Method GET)
* blogs/?search=слово1+слово2

Получить отсортированный по дате список статей, в которых есть тег1 и одновременно тег2
* blogs/?ordering=-created_at&tags=тег1%2C+тег2

Получить отсортированный по популярности список статей, в которых есть тег1 и одновременно тег2
* blogs/?tags=тег1%2C+тег2

Получить определенную статью, зная ее slug (Method GET)
* blogs/***slug***/

Получить список комментариев определенной статьи по slug (Method GET)
* blogs/***slug***/comments/

Получить по id комментарий
* comments/***int***/

Лайкнуть по id комментарий (Method POST)
* comments/***int***/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/***int***/dislike/

Лайкнуть по slug статью (Method POST)
* blogs/***slug***/like/

Дизълайкнуть по slug статью (Method POST)
* blogs/***slug***/dislike/

Сохранить по slug статью (Method POST)
* blogs/***slug***/save/

Вывести колличество статей (Method GET)
* count/blogs/

Вывести список свежих статей (Method GET)
* blogs_fresh/

Вывести список лучших статей (Method GET)
* blogs_best/

Вывести список горячих статей (Method GET)
* blogs_hot/

Вывести список непросмотренных статей (Method GET)
* blogs_nonviewed/

Вывести список рекомендуемых статей (Method GET)
* blogs_recommend/

2. IMAGE
Апи по по работе с Картинками

Вывести список картинок (Method GET)
* images/

Сохранить картинку (Method POST)
* images/

3. USER (Апи касаемо юзера)
Апи по по работе с Юзерами

Вывести информацию о себе (Method GET)
* user/

Вывести список пользователей (Method GET)
* user_all/

Вывести список своих сохраненных статей (Method GET)
* user/saved/blogs/

Вывести список своих понравившихся статей (Method GET)
* user/liked/blogs/

Вывести список своих созданных статей (Method GET)
* user/created/blogs/

- Вывести список своих понравившихся комментариев статей (Method GET)
* user/liked/blogs/comment/

- Вывести список своих созданных комментариев статей (Method GET)
* user/created/blogs/comment/

- Вывести список своих сохраненных отчетов (Method GET)
* user/saved/report/

- Вывести список своих понравившихся отчетов (Method GET)
* user/liked/report/

- Вывести список своих созданных отчетов (Method GET)
* user/created/report/

- Вывести список своих понравившихся комментариев отчетов (Method GET)
* user/liked/report/comment/

- Вывести список своих созданных комментариев отчетов (Method GET)
* user/created/report/comment/

Вывести информацию о юзере по логину (Method GET)
* user_select/***username***/

Вывести список созданных отчетов юзера по логину (Method GET)
* user_select_reports/created_by/***username***/

Вывести список созданных блогов юзера по логину (Method GET)
* user_select_blogs/created_by/***username***/

Подписаться на определенного юзера (Method POST)
* user_select/***username***/subscript/

Вывести колличество юзеров (Method GET)
* count/user/

Вывести сортированный список юзеров по социальному и по рыболовному рейтингу (Method GET)
n - начальный элемент (от 1 до ...)
k - шаг (на сколько много юзеров от начального) (от 0 до ...)
Если n+k>числа пользователей, то будет ошибка в виде одной строки error 
Например:
n=5, k=2 это вывести 5,6,7
n=5, k=0 это вывести 5
* user_top_social_rating/***n***/***k***/
* user_top_fishing_rating/***n***/***k***/


Обновить информацию о пользователе (GET + PUT)
* update_user_info/

Залогинется (Method POST)
* dj-rest-auth/login/

Зарегистрироваться (Method POST)
* dj-rest-auth/registration/

Работа с токенами
* dj-rest-auth/token/refresh/

3. REPORT
Апи по по работе с Отчетами

Вывести список отчетов (Method GET)
* report/

Получить список отчетов в которых есть одновременно слово1 и слово2 (Method GET)
* report/?search=слово1+слово2

Получить отсортированный по дате список отчетов, в которых есть тег1 и одновременно тег2
* report/?ordering=-created_at&tags=тег1%2C+тег2

Получить отсортированный по популярности список отчетов, в которых есть тег1 и одновременно тег2
* report/?tags=тег1%2C+тег2

Получить определенный отчет, зная его slug (Method GET)
* report/***slug***/

Получить список комментариев определенного отчета по slug (Method GET)
* report/***slug***/comments/

Получить по id комментарий
* comments/***int***/

Лайкнуть по id комментарий (Method POST)
* comments/***int***/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/***int***/dislike/

Лайкнуть по slug статью (Method POST)
* report/***slug***/like/

Дизълайкнуть по slug статью (Method POST)
* report/***slug***/dislike/

Вывести колличество отчетов (Method GET)
* count/reports/

4. NEWS
Апи по по работе с Новостями

Вывести список Новостей (Method GET)
* news/

Получить список новостей в которых есть одновременно слово1 и слово2 (Method GET)
* news/?search=слово1+слово2   (поиск таким образом, чтобы одновременно два слова были) 

Получить определенную новость, зная ее slug (Method GET)
* news/***slug***/

Получить список комментариев определенной новости по slug (Method GET)
* news/***slug***/comments/

Получить по id комментарий
* comments/***int***/

Лайкнуть по id комментарий (Method POST)
* comments/***int***/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/***int***/dislike/

Лайкнуть по slug новость (Method POST)
* news/***slug***/like/

Дизълайкнуть по slug статью (Method POST)
* news/***slug***/dislike/

Вывести колличество новостей (Method GET)
* count/news/

5. SPACE
Апи по по работе с водными ресурсами и регионами

Вывести список Регионов (Method GET)
* region/

Получить список регионов в которых есть одновременно слово1 и слово2 (Method GET)
* region/?search=слово1+слово2   (поиск таким образом, чтобы одновременно два слова были) 

Получить определенный регион, зная его slug (Method GET)
* region/***slug***/

Вывести список Платных водоемов (Method GET)
* waterplace_cost/

Получить список платных водоемов в которых есть одновременно слово1 и слово2 (Method GET)
* waterplace_cost/?search=слово1+слово2   (поиск таким образом, чтобы одновременно два слова были) 

Получить определенный платный водоем, зная его slug (Method GET)
* waterplace_cost/***slug***/

Вывести список Платных водоемов (Method GET)
* waterplace_nature/

Получить список природных водоемов в которых есть одновременно слово1 и слово2 (Method GET)
* waterplace_nature/?search=слово1+слово2   (поиск таким образом, чтобы одновременно два слова были) 

Получить определенный природный водоем, зная его slug (Method GET)
* waterplace_nature/***slug***/

Вывести колличество платных водоемов (Method GET)
* count/waterplace_cost/

Вывести колличество природных водоемов (Method GET)
* count/waterplace_nature/

Вывести колличество регионов (Method GET)
* count/region/

6. Иные Модели
Апи по по работе с иными моделями
* statistics_main_page/

Список тегов (пополняемый) + поиск
* tags/

Список методов ловли (пополняемый) + поиск
* fishing_method/

Список наконечников (пополняемый) + поиск
* nozzles/



Frontend 

go to folder "frontend"

write npm install

run it npm run serve

RUN SERVER

в папке fishow_django когда виртуальное окружение активно

python manage.py runserver

во втором терминале в папке frontend

npm run serve

адресс использовать джанговский, на маке возможно надо заменить на 0.0.0.0:8000
