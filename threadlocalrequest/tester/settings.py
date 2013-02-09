# Stripped-down Django settings for testrunner

DEBUG = True

SECRET_KEY = 'NOT_SO_SECRET'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'threadlocalrequest.middleware.ThreadLocalMiddleware'
)

TEST_RUNNER = 'testrunner.NoDbTestRunner'
ROOT_URLCONF = 'tester.urls'
INSTALLED_APPS = (
    'tester',
)




