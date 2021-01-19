import re
from django_python3_ldap import utils


def auth_username_format(model_fields):
    return utils.format_username_active_directory(model_fields)


def auth_attrs_matched(ldap_attributes):
    """
    is_ou_matched_regex determine the account is RockGP or 磐石保經
    is_account_matched_regex determine the account is allowed,
    system account is not matched.
    """
    is_ou_matched_regex: str = ".+,OU=(RockGP|磐石保經),.+"
    is_account_matched_regex: str = "[A|E|Z|a|e|z].{6}"
    dn: str = ldap_attributes["distinguishedName"][0]
    account_name: str = ldap_attributes["sAMAccountName"][0]
    is_ou_matched = re.match(is_ou_matched_regex, dn)
    is_account_matched = re.match(is_account_matched_regex, account_name)
    return is_ou_matched and is_account_matched


def auth_sync_user(user, ldap_attributes):
    user.is_active = True
    user.is_staff = True
    user.save()