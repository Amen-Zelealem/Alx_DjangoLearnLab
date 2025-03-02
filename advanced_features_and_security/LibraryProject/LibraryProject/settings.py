"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qgy4mjey$e=!g4sh^vgofa^pxfa3=s7g@hw8807t-t(%s9m-1v"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking attacks
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME sniffing attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies are only sent over HTTPS in production
CSRF_COOKIE_SECURE = True  # Only send CSRF cookies over HTTPS
SESSION_COOKIE_SECURE = True  # Only send session cookies over HTTPS


# Enforce HTTPS on all connections by redirecting HTTP to HTTPS
SECURE_SSL_REDIRECT = True  # This will redirect all HTTP requests to HTTPS

# HTTP Strict Transport Security (HSTS) settings
# This ensures browsers only communicate with your site over HTTPS
SECURE_HSTS_SECONDS = 31536000  # One year (in seconds)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains as well
SECURE_HSTS_PRELOAD = True  # Allow this site to be preloaded in the browser's HSTS list


# Prevent clickjacking by setting the X-Frame-Options header to DENY
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from sniffing the MIME type and interpreting content differently than declared
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filtering to prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True


AUTH_USER_MODEL = 'bookshelf.CustomUser'


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
    "relationship_app",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
