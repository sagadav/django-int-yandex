[![Python package](https://github.com/sagadav/django-int-yandex/actions/workflows/python-package.yml/badge.svg?branch=dev)](https://github.com/sagadav/django-int-yandex/actions/workflows/python-package.yml)

Инструкция

### Запуск в Dev mode:

1. Настройте виртуальное окружение, пример:

```
python -m venv venv
```

2. Создайте файл .env с переменными окружения (пример: .env.example)
3. Установите зависимости и запустите (пример для Windows):

```
pip install -r requirements\dev.txt
cd lyceumsite
py manage.py runserver
```

Переменные окружения:

```
SECRET_KEY - секретный ключ
DEBUG - режим дебага
ALLOWED_HOSTS - разрешенные хосты
```

Django v3.2
Python v3.11
