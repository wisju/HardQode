# Тестовое задание Backend/Django

## Построение системы для обучения

### Построение архитектуры

В этом задании у нас есть три бизнес-задачи на хранение:
1. Создать сущность продукта. У продукта должен быть создатель этого продукта(автор/владелец). Название продукта, дата и время старта, стоимость
2. Определить, каким образом мы будем понимать, что у пользователя(клиент/студент) есть доступ к продукту.
3. Создать сущность урока. Урок может принадлежать только одному продукту. В уроке должна быть базовая информация: название, ссылка на видео.
4. Создать сущность группы. По каждому продукту есть несколько групп пользователей, которые занимаются в этом продукте. Минимальное и максимальное количество юзеров в группе задается внутри продукта. Группа содержит следующую информацию: ученики, которые состоят в группе, название группа, принадлежность группы к продукту.
Использовать Django

### Написание запросов и реализация логики распределения 
Написание запросов и реализация логики распределения 
В этом пункте потребуется использовать выполненную вами в прошлом задании архитектуру:
1. При получении доступа к продукту, распределять пользователя в группу. Если продукт ещё не начался, то можно пересобрать группы так, чтобы везде было примерно одинаковое количество участников. По умолчанию алгоритмы распределения должен работать заполняя до максимального значения.
 + Доп задания дается на реализацию алгоритма распределения по группам так, чтобы в каждой группе количество участников не отличалось больше, чем на 1. При этом, минимальные и максимальные значения участников в группе должны быть учтены
2. Реализовать API на список продуктов, доступных для покупки, которое бы включало в себя основную информацию о продукте и количество уроков, которые принадлежат продукту.
3. Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ.


## Installation

`python -m venv venv`

#### Windows
`venv/Scripts/activate`

#### Unix
`source venv/bin/activate`

## Install Dependencies
`pip install -r requirements.txt`

## Run

`python manage.py runserver`

## Info
`python manage.py createsuperuser`
+ superuser: admin 
+ password: admin
