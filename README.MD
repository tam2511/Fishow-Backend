`.\env\Scripts\activate`

`python manage.py runserver`

**Backend**

1. `cd fishow_django`

2. `python -m venv env`

3. Activate env

4. `pip install -r requirements.txt`

~ `python3 manage.py migrate --run-syncdb`

**API**

127.0.0.1/api/...

1. BLOGS,COMMENTS,IMAGE
* blogs/
* images/
* blogs/<slug:slug>/comments/
* blogs/<slug:slug>/comment/
* comments/<int:pk>/
* comments/<int:pk>/like/
* comments/<int:pk>/dislike/
* blogs/<slug:slug>/like/
* blogs/<slug:slug>/dislike/
* blogs/<slug:slug>/save/

2. USER
* user/
* user_all/
* user/saved/blogs/
* user/liked/blogs/
* user/created/blogs/
* user/liked/blogs/comment/
* user/created/blogs/comment/
* user/saved/report/
* user/liked/report/
* user/created/report/
* user/liked/report/comment/
* user/created/report/comment/
* user_select/(?P<username>.*)/
* user_select/(?P<username>.*)/subscript/

* rest-auth/login/
* rest-auth/registration/

3. REPORT
* report/
* report/<slug:slug>/comments/
* report/<slug:slug>/comment/
* comments/<int:pk>/
* comments/<int:pk>/like/
* comments/<int:pk>/dislike/
* report/<slug:slug>/like/
* report/<slug:slug>/dislike/

4. NEWS
* news/
* news/<slug:slug>/comments/
* news/<slug:slug>/comment/
* comments/<int:pk>/
* comments/<int:pk>/like/
* comments/<int:pk>/dislike/
* news/<slug:slug>/like/
* news/<slug:slug>/dislike/

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




