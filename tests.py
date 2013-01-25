"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import TestCase, RequestFactory, Client
from threadlocalrequest.threadlocals import set_thread_variable, get_thread_variable, get_current_request, get_current_session


def set_request_threadlocal(request, host="testserver"):
    if host:
        request.META['HTTP_HOST'] = host  # allows for testing host-related things
    set_thread_variable('request', request)

def set_current_user(site = None, superuser=False):
    request = get_current_request()
    request.user = TenantSiteUser.objects.get_or_create(username='bob', site = site)[0]
    if superuser:
        request.user.is_superuser = True

def add_session_to_current_request():
    c = Client()
    request = get_current_request()
    request.session = c.session

class ThreadlocalsTest(TestCase):

    def setUp(self):
        from threading import local
        self._threadlocals = local()
        self.factory = RequestFactory()
        set_thread_variable('request', None)

    def tearDown(self):
        set_thread_variable('request', None)

    def test_get_thread_variable_default(self):
        gotten = get_thread_variable('unset', 'default value')
        self.assertEqual(gotten, 'default value')

    def test_get_set_thread_variable(self):
        set_thread_variable('test', { 'test': 'test'})
        gotten = get_thread_variable('test')
        self.assertEqual(gotten, { 'test': 'test'})

    def test_get_current_request(self):
        self.assertEqual(get_current_request(), None)  # tests default (None)
        request = self.factory.get('/')
        set_request_threadlocal(request)
        self.assertEqual(get_current_request(), request)

    def test_get_current_session(self):
        pass

    def test_get_current_user(self):
        pass


class ThreadLocalMiddlewareTest(TestCase):

    def test_process_request(self):
        """
        if ThreadLocalMiddleware is enabled in settings, then running the test client
        should trigger the middleware and set the request in thread locals
        """
        self.client.get('/heartbeat/')
        self.assertEqual(get_current_request().path, u'/heartbeat/')
