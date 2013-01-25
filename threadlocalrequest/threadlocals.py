# -*- coding: utf-8 -*-
"""
__init__ module for the threadlocals package

Derived from django-threaded-multihost (see license.txt)
"""
__docformat__="restructuredtext"

import logging

log = logging.getLogger('threadlocalrequest.middleware')

from threading import local

_threadlocals = local()

def get_current_request():
    return get_thread_variable('request', None)

def get_current_session():
    req = get_current_request()
    if req is None:
        return None
    return req.session
    
def get_current_user():
#    user = get_thread_variable('user', None)
#    if user != None: return user
    req = get_current_request()
    if req == None or not hasattr(req, 'user'): return None
    return req.user

def set_current_user(user):
    set_thread_variable('user', user)

def set_thread_variable(key, var):
    setattr(_threadlocals, key, var)
    
def get_thread_variable(key, default=None):
    return getattr(_threadlocals, key, default)