# BrendWall_test
Реализовано Django-приложение, где
API для работы с продуктами (создание и получение списка).
Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.

### Как запустить:
Файл envExample переименовать в .env. Поменять значения переменных окружения в соответствии со своими параметрами системы

#### Локально
pip install -r requirements.txt
python ./brendwall_project/manage.py migrate
python ./brendwall_project/manage.py runserver
```

Сервис будет доступен по адресу http://localhost:8000
