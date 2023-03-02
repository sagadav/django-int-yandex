[![Python package](https://github.com/sagadav/django-int-yandex/actions/workflows/python-package.yml/badge.svg?branch=dev)](https://github.com/sagadav/django-int-yandex/actions/workflows/python-package.yml)

Инструкция

### Запуск в Dev mode (Windows):

1. Настройте виртуальное окружение, пример:

```cmd
python -m venv venv
```

2. Создайте файл .env с переменными окружения (пример: .env.example)
3. Установите зависимости и запустите:

```cmd
pip install -r requirements\dev.txt
cd lyceumsite
py manage.py runserver
```

### Переменные окружения:

```
SECRET_KEY - секретный ключ
DEBUG - режим дебага
ALLOWED_HOSTS - разрешенные хосты
```

### Работа с фикстурами (Fixtures):
#### Windows:  
load:
```cmd
py lyceumsite\manage.py loaddata fixtures\data.json
```
dump:
```cmd
python -Xutf8 lyceumsite\manage.py dumpdata APP_NAME --indent=4 > fixtures\data.json
```

### Запуск тестов:  
Windows:
```cmd
cd lyceumsite
py manage.py test
```

Django v3.2
Python v3.11
