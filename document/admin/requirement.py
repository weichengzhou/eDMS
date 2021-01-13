
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import traceable, suspendable
from core.admin.base import edms_admin
from .core import DocumentAdmin
from ..forms.requirement import RequirementDocumentForm
from ..models.requirement import RequirementDocument


# @admin.register(RequirementDocument)
class RequirementDocumentAdmin(DocumentAdmin,
    traceable.TraceableAdmin,
    suspendable.SuspendableAdmin):

    list_display = ['document_seq', 'document_name_link', 'apply_date']

    fieldsets = ((None, {
            'fields': ('document_seq', 'document', 'apply_date')
        }),
    )

    form = RequirementDocumentForm

edms_admin.register(RequirementDocument, RequirementDocumentAdmin)