

from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from core.admin import traceable, suspendable, fields
from core.admin.base import edms_admin
from .core import DocumentAdmin
from ..forms.checkout import CheckoutDocumentForm
from ..models.checkout import CheckoutDocument


class CheckoutDocumentAdmin(DocumentAdmin,
    traceable.TraceableAdmin,
    suspendable.SuspendableAdmin):

    list_display = ['document_seq', 'document_name_link',
        'relyon_requirement_name_link', 'apply_date']

    fieldsets = ((None, {
        'fields': ('relyon_requirement', 'document', 'apply_date'),
        }),
    )

    form = CheckoutDocumentForm

    def relyon_requirement_name_link(self, obj):
        if obj.relyon_requirement is None:
            return None
        else:
            document_seq = obj.relyon_requirement.document_seq
            document_url = fields.get_reverse_link(
                'admin:document_requirementdocument_change',
                [document_seq]
            )
            html_link = fields.get_html_link(document_url, document_seq)
            return format_html(html_link)


    relyon_requirement_name_link.short_description = _('申請依據 (需求單號)')


edms_admin.register(CheckoutDocument, CheckoutDocumentAdmin)