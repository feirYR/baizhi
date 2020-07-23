"""
Django settings for baizhi_drf project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bhzfo^c&rvfsh*#ac6#iyi3^a$9)hl_t40dx(7%f)4&8*tar)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "api.baizhishop.com",
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'home',
    'user',
    'course',
    'order',
    'payments',
    # 'django_celery_results',
    # 'ckeditor',
    # 'ckeditor-uploader'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'baizhi_drf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'baizhi_drf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'baizhi_db',
        # 'USER': 'root',
        # 'PASSWORD':'123456',
        # 'HOST':'localhost',
        # 'PORT':3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
AUTH_USER_MODEL = 'user.UserInfo'

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "utils.exceptions.my_exception_handler",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
    ]
}
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler'
}
AUTHENTICATION_BACKENDS = ['user.utils.UserAuthModelBackend']

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",  # Redis缓存入口，其中使用DefaultClient操作缓存
        "LOCATION": "redis://192.168.42.133:7000/0",  # ip:port/db_index
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"  # 操作缓存的对象
        }
    },
    "sms": {
        "BACKEND": "django_redis.cache.RedisCache",  # Redis缓存入口，其中使用DefaultClient操作缓存
        "LOCATION": "redis://192.168.42.133:7000/1",  # ip:port/db_index
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"  # 操作缓存的对象
        }
    },
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",  # Redis缓存入口，其中使用DefaultClient操作缓存
        "LOCATION": "redis://192.168.42.133:7000/2",  # ip:port/db_index
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"  # 操作缓存的对象
        }
    },
    "review": {
        "BACKEND": "django_redis.cache.RedisCache",  # Redis缓存入口，其中使用DefaultClient操作缓存
        "LOCATION": "redis://192.168.42.133:7000/5",  # ip:port/db_index
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"  # 操作缓存的对象
        }
    }
}

# 支付宝配置信息
ALIAPY_CONFIG = {
    # "gateway_url": "https://openapi.alipay.com/gateway.do?", # 真实支付宝网关地址
    "gateway_url": "https://openapi.alipaydev.com/gateway.do?",  # 沙箱支付宝网关地址
    "appid": "2016102200738366",
    "app_notify_url": None,
    "app_private_key_path": open(os.path.join(BASE_DIR, "apps/payments/keys/app_private_key.pem")).read(),
    "alipay_public_key_path": open(os.path.join(BASE_DIR, "apps/payments/keys/app_private_key.pem")).read(),
    "sign_type": "RSA2",
    "debug": False,
    # "return_url": "http://www.baizhistore.cn:8080/payments/result",  # 同步回调地址
    "return_url": "http://localhost:8080/payments/result",  # 同步回调地址
    "notify_url": "http://api.baizhishop.com:8000/payments/result",  # 异步结果通知
}

# KEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',	# 展示哪些工具栏
#         'height': 300,	# 编辑器的高度
#         # 'width': 300,
#     },
# }
# CKEDITOR_UPLOAD_PATH = "uploads/"

#celery返回结果配置
# CELERY_BROKER_URL = 'redis://192.168.42.133:7000/3'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'redis://192.168.42.133:7000/4'
# # CELERY_RESULT_BACKEND = 'django-db'
# CELERY_TIMEZONE = 'Asia/Shanghai'

# 项目的日志配置
LOGGING = {
    # 版本
    'version': 1,
    # 是否禁用已存在的日志器
    'disable_existing_loggers': False,
    # 格式化日志信息
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    # 日志的过滤信息
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理日志的方法
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            # 记录到文件中的日志等级
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置  日志的文件名  日志的保存目录
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/lesson_api.log"),
            # 日志文件的大小  100M
            'maxBytes': 100 * 1024 * 1024,
            # 日志文件的最大数量
            'backupCount': 10,
            # 日志的格式
            'formatter': 'verbose'
        },
    },
    # 日志对象，与django集成使用
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}
