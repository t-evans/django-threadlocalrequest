Setup/Usage
===========

Add "threadlocalrequest.middleware.ThreadLocalMiddleware" to your MIDDLEWARE_CLASSES setting.
Then use it as follows:

Example usage:
--------------
`from threadlocalrequest.threadlocals import get_current_request

request = get_current_request()`


Caveat Emptor
==================

Storing the request in threadlocals goes against several django core developers' strong inclinations against using threadlocals.
See [this thread on django-users](https://groups.google.com/forum/?fromgroups=#!topic/django-users/5681nX0YPgQ) for a more in-depth discussion.
We recommend you not do this unless you have a really good reason to do so. We feel like we had a really good
reason (the only one we've come across so far):
Having the request in threadlocals is the core piece that allowed us to build a true multi-tenant system on top of django where the site is resolved dynamically based on the current host,
and  objects are filtered based on the current host. With the current version of django, this is nearly impossible to do without the request in threadlocals.  This was a very significant and advanced undertaking, but we're happy with the results.


Tests
-----

To run tests:

python tester/manage.py test

