`.\env\Scripts\activate`

`python manage.py runserver`

**Backend**

1. `cd fishow_django`

2. `python -m venv env`

3. Activate env

4. `pip install -r requirements.txt`

~ `python manage.py migrate --run-syncdb`

**Frontend** 

go to folder `"frontend"`

write `npm install`

run it `npm run serve`

**RUN SERVER**

в папке fishow_django когда виртуальное окружение активно

`python manage.py runserver`

во втором терминале в папке frontend

`npm run serve`

адресс использовать джанговский, на маке возможно надо заменить на `0.0.0.0:8000`


в джанго: 

1. нужно что бы у блога можно было приписать теги
2. у блога будет добавить лайки по такой же схеме как у комментариев
3. добавить в модель так же счетчик просмотров (все работать будет на фронте, нужно ли куда записывать значение)
4. Добавить поле которое говорит что это блог либо это статья ( будет указыватся при создании ) 
