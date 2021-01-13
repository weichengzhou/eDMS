
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _

class EDMSAdminSite(AdminSite):
    site_title = _('EDMS 文件管理系統')
    site_header = _('EDMS 文件管理系統')
    index_title = _('EDMS 管理介面')

edms_admin = EDMSAdminSite()