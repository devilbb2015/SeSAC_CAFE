# my_settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

## 로컬에서 IP로 연결
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'cafe',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '192.168.10.226',
#         'PORT': '3306',
#     },
#     'common': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     },
#
# }

## 로컬 호스트에서 연결
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cafe',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    # 'common': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },

}