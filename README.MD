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

Получить определенную статью, зная ее slug (Method GET)
* blogs/***slug***/

Получить список комментариев определенной статьи по slug (Method GET)
* blogs/***slug***/comments/

Получить по id комментарий
* comments/<int>/

Лайкнуть по id комментарий (Method POST)
* comments/<int>/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/<int>/dislike/

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
* user_select/<username>/

Подписаться на определенного юзера (Method POST)
* user_select/<username>/subscript/

Вывести колличество юзеров (Method GET)
* count/user/

Залогинется (Method POST)
* rest-auth/login/

Зарегистрироваться (Method POST)
* rest-auth/registration/

3. REPORT
Апи по по работе с Отчетами

Вывести список отчетов (Method GET)
* report/

Получить список отчетов в которых есть одновременно слово1 и слово2 (Method GET)
* report/?search=слово1+слово2

Получить определенный отчет, зная его slug (Method GET)
* report/***slug***/

Получить список комментариев определенного отчета по slug (Method GET)
* report/***slug***/comments/

Получить по id комментарий
* comments/<int>/

Лайкнуть по id комментарий (Method POST)
* comments/<int>/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/<int>/dislike/

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
* comments/<int>/

Лайкнуть по id комментарий (Method POST)
* comments/<int>/like/

Дизълайкнуть по id комментарий (Method POST)
* comments/<int>/dislike/
