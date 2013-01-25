Add "threadlocalrequest.middleware.ThreadLocalMiddleware" to your MIDDLEWARE_CLASSES setting.

Example usage:

from threadlocalrequest.threadlocals import get_current_request
request = get_current_request()
