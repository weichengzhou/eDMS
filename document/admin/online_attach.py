

from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from core.admin import traceable, suspendable, fields
from core.admin.base import edms_admin
from .core import DocumentAdmin
from ..forms.online_attach import OnlineAttachmentForm
from ..models.online_attach import OnlineAttachment


class OnlineAttachmentAdmin(DocumentAdmin,
    traceable.TraceableAdmin,
    suspendable.SuspendableAdmin):

    list_display = ['document_seq', 'document_type', 'document_name_link']

    fieldsets = ((None, {
        'fields': ('document', 'document_type')
        }),
    )

    form = OnlineAttachmentForm


edms_admin.register(OnlineAttachment, OnlineAttachmentAdmin)