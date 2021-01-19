
from django_python3_ldap import auth

from . import ldap

class LDAPBackend(auth.LDAPBackend):
    
    def authenticate(self, *args, **kwargs):
        return ldap.authenticate(*args, **kwargs)