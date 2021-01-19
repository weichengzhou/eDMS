"""
Settings used by django-python3.
"""

from django.conf import settings

from django_python3_ldap.conf import LazySettings


class LazySetting(object):

    """
    A proxy to a named Django setting.
    """

    def __init__(self, name, default=None):
        self.name = name
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return getattr(obj._settings, self.name, self.default)


class LazySettings(LazySettings):
    
    LDAP_AUTH_ATTRS_IS_MATCHED = LazySetting(
        name="LDAP_AUTH_ATTRS_IS_MATCHED",
        default=None
    )

settings = LazySettings(settings)