# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong

# Based on part of the tornado framework

# Fake unicode literal support:  Python 3.2 doesn't have the u'' marker for
# literal strings, and alternative solutions like "from __future__ import
# unicode_literals" have other problems (see PEP 414).  u() can be applied
# to ascii strings that include \u escapes (but they must not contain
# literal non-ascii characters).
if type('') is not type(b''):
    def u(s):
        return s
    bytes_type = bytes
    unicode_type = str
    basestring_type = str
else:
    def u(s):
        return s.decode('unicode_escape')
    bytes_type = str
    unicode_type = unicode
    basestring_type = basestring


_UTF8_TYPES = (bytes_type, type(None))


def _utf8(value):
    """Converts a string argument to a byte string.

    If the argument is already a byte string or None, it is returned unchanged.
    Otherwise it must be a unicode string and is encoded as utf8.
    """
    if isinstance(value, _UTF8_TYPES):
        return value
    if not isinstance(value, unicode_type):
        raise TypeError(
            "Expected bytes, unicode, or None; got %r" % type(value)
        )
    return value.encode("utf-8")


_TO_UNICODE_TYPES = (unicode_type, type(None))


def _unicode(value):
    """Converts a string argument to a unicode string.

    If the argument is already a unicode string or None, it is returned
    unchanged.  Otherwise it must be a byte string and is decoded as utf8.
    """
    if isinstance(value, _TO_UNICODE_TYPES):
        return value
    if not isinstance(value, bytes_type):
        raise TypeError(
            "Expected bytes, unicode, or None; got %r" % type(value)
        )
    return value.decode("utf-8")


# When dealing with the standard library across python 2 and 3 it is
# sometimes useful to have a direct conversion to the native string type
if str is unicode_type:
    native_str = _unicode
else:
    native_str = _utf8

_BASESTRING_TYPES = (basestring_type, type(None))


def to_utf8(obj):
    """Walks a simple data structure, converting unicode to byte string.

    Supports lists, tuples, and dictionaries.
    """
    if isinstance(obj, unicode_type):
        return _utf8(obj)
    elif isinstance(obj, dict):
        return dict((to_utf8(k), to_utf8(v)) for (k, v) in obj.items())
    elif isinstance(obj, list):
        return list(to_utf8(i) for i in obj)
    elif isinstance(obj, tuple):
        return tuple(to_utf8(i) for i in obj)

    return obj


def to_unicode(obj):
    """Walks a simple data structure, converting byte strings to unicode.

    Supports lists, tuples, and dictionaries.
    """
    if isinstance(obj, bytes_type):
        return _unicode(obj)
    elif isinstance(obj, dict):
        return dict((to_unicode(k), to_unicode(v)) for (k, v) in obj.items())
    elif isinstance(obj, list):
        return list(to_unicode(i) for i in obj)
    elif isinstance(obj, tuple):
        return tuple(to_unicode(i) for i in obj)

    return obj
