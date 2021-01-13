
import abc

from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from core.admin import fields
from ..models.core import Document

class DocumentTabularInline(admin.TabularInline):
    
    
    def document_name_link(self, obj):
        if obj.document_seq is None:
            return None
        else:
            document_url = fields.get_reverse_link(
                'admin:document_onlineattachment_change',
                [obj.document_seq]
            )
            document_name = obj.document_name()
            html_link = fields.get_html_link(document_url, document_name)
            return format_html(html_link)

    document_name_link.short_description = _('文件名稱')


class DocumentAdmin(admin.ModelAdmin):
    
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
    

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


    def get_form(self, request, obj=None, change=False, **kwargs):
        return super().get_form(request, obj, change, **kwargs)


    def document_name_link(self, obj):
        document_url = settings.MEDIA_URL + str(obj.document)
        document_name = obj.document_name()
        html_link = fields.get_html_link(document_url, document_name)
        return format_html(html_link)
    

    document_name_link.short_description = _('檔案名稱')