## 2022-MAI-Backend-D-Ivanova
Лабораторные работы по программной инженерии


## Лабораторная работа 1

- Завести репозиторий на github, установить Python (>=3.6) (2 балла)
- Создать виртуальное окружение для Python и установить Django==4 (1 балл)
- Описать зависимости в requirements.txt (1 балл)
- Создать правильный .gitignore файл и оформить изменения в виде отдельных осмысленных коммитов (1 балл)
- Написать реализацию LRU-cache на языке Python (5 баллов)  

> cd ./LRUcache

> python3 main.py

## Лабораторная работа 2

- Установить nginx и gunicorn — 2 балла;
- Настроить nginx для отдачи статический файлов из public/ — 2 балла;
- Создать простейшее WSGI-приложение и запустить его с помощью gunicorn — 2 балла;
- Настроить проксирование запросов на nginx — 2 балла;
- Измерить производительность nginx и gunicorn c помощью ab или wrk — 2 балла.

> source ~/venv/bin/activate

> gunicorn --workers 4 myapp:app


```
user@user-virtual-machine:~/Desktop/2022-MAI-Backend-D-Ivanova$ wrk -t12 -c400 -d30s http://localhost/public/index.html
Running 30s test @ http://localhost/public/index.html
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   121.65ms  237.17ms   1.26s    86.17%
    Req/Sec     1.51k   506.29     4.20k    70.70%
  536980 requests in 30.10s, 193.55MB read
Requests/sec:  17840.04
Transfer/sec:      6.43MB
```

```
wrk -t12 -c400 -d30s http://localhost/backend/
Running 30s test @ http://localhost/backend/
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   202.06ms   76.41ms 681.07ms   86.35%
    Req/Sec   170.78     99.27   740.00     59.54%
  60370 requests in 30.10s, 10.59MB read
Requests/sec:   2005.82
Transfer/sec:    360.36KB
```

```
wrk -t12 -c400 -d30s http://localhost:8000
Running 30s test @ http://localhost:8000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   218.85ms  163.26ms   1.24s    89.29%
    Req/Sec   180.56    107.43   460.00     52.77%
  60150 requests in 30.08s, 9.52MB read
Requests/sec:   1999.65
Transfer/sec:    324.18KB
```


## Лабораторная работа 3

- Создать и запустить Django-проект — 2 балла;
- Реализовать «заглушки» для всех методов API, используя JsonResponse  — 3 баллов:
- В конфиге nginx создать location, которое будет ходить на Django-приложение — 3 балла
- Обрабатывать только нужные методы (GET/POST) — 2 балла.

## Лабораторная работа 4

- Установить Postgres, создать нового пользователя и БД и настроить доступ — 5 баллов;
- Спроектировать базу данных проекта, подготовить модели и мигрировать их в БД — 5 баллов;
- должна присутствовать как минимум одна из связей OneToOne, ForeignKey, ManyToMany)

## Лабораторная работа 5

- Реализовать методы для:
a. Поиска пользователей
b. Создания персонального чата
c. Получения списка чатов

## Лабораторная работа 6

- Установить docker и docker-compose (1 балл);
- Создание Dockerfile для Django приложения (2 балла);
- Создание docker-compose для проекта:
a. nginx (3 балла),
b. База данных (3 балла),
- Создание Makefile для проекта (1 балл);

> Преподаватель должен иметь возможность, имея установленными только git, docker и docker-compose склонировать проект, выполнить команды `make migrate` и увидеть успешную миграцию.

## Лабораторная работа 7

- Добавить в проект djangorestframework;
- Переписать заглушки всех предыдущих методов;
- Написать один или несколько форм для валидации форм.
