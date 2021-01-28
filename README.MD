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
* blogs/<slug>/
* images/
* blogs/<slug>/comments/
* blogs/<slug>/comment/
* comments/<int>/
* comments/<int>/like/
* comments/<int>/dislike/
* blogs/<slug>/like/
* blogs/<slug>/dislike/
* blogs/<slug>/save/
* count/blogs/

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
* user_select/<username>/
* user_select/<username>/subscript/
* count/user/

* rest-auth/login/
* rest-auth/registration/

3. REPORT
* report/
* report/<slug>/
* report/<slug>/comments/
* report/<slug>/comment/
* comments/<int>/
* comments/<int>/like/
* comments/<int>/dislike/
* report/<slug>/like/
* report/<slug>/dislike/
* count/reports/

4. NEWS
* news/
* news/<slug>/
* news/<slug>/comments/
* news/<slug>/comment/
* comments/<int>/
* comments/<int>/like/
* comments/<int>/dislike/
* news/<slug>/like/
* news/<slug>/dislike/
* count/news/

5. SPACE
* region/
* region/<slug>
* waterplace_cost/
* waterplace_cost/<slug>
* waterplace_nature/
* waterplace_nature/<slug>

* count/waterplace_cost/
* count/waterplace_nature/
* count/region/


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




