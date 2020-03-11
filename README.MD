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

