установка фронтенда: 

терминал открыт в папке frontend3_1/frontend3

при первоначальной установке либо когда были добавленые новые пакеты: 
~~~ 
npm install
~~~ 
далее, сборка фронтенда 
~~~ 
npm run build
~~~ 
запускаем **фронтенд**, сервер будет запущен по адресу **http://localhost:3000/**
~~~
npm run start 
~~~

в папке fishow_django ( backend )

устанавлием зависимости 

~~~
pip3 install -r requirements.txt
~~~

~~~
pip3 install django-cors-headers
~~~

после идут миграции и т.д.

затем

собираем файлы с помощью collectstatic

~~~ 
python3 manage.py collectstatic 
~~~

и запускаем бек (как это делается в докере хз)

~~~ 
python3 manage.py runserver
~~~
