
from typing import Iterable, List

from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from core.admin import traceable, suspendable, fields
from core.admin.base import edms_admin

from .core import DocumentAdmin, DocumentTabularInline
from ..forms.online import OnlineDocumentForm
from ..models.online import OnlineDocument
from ..models.requirement import RequirementDocument
from ..models.online_attach import OnlineAttachment

class OnlineAttachmentInline(DocumentTabularInline,
    traceable.TraceableTabularInline,
    suspendable.SuspendableTabularInline):
    model = OnlineAttachment
    extra = 1
    fields = ('document_name_link', 'document_type', 'document')
    readonly_fields = ('document_name_link',)
    

class OnlineDocumentAdmin(DocumentAdmin,
    traceable.TraceableAdmin,
    suspendable.SuspendableAdmin):
    
    list_display = ['document_seq', 'document_name_link', 
        'relyon_requirement_name_link', 'apply_date']

    fieldsets = ((None, {
            'fields': ('document_seq', 'document', 'relyon', 'apply_date')
        }),
    )

    form = OnlineDocumentForm
    

    inlines = [OnlineAttachmentInline,]


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.save_relyon(obj, form.cleaned_data['relyon'])
    

    def save_relyon(self, online_document: OnlineDocument,
        requirement_documents: Iterable[RequirementDocument]):
        # Clear all relyon relationship.
        online_document.clear_relyon_requirement()
        for requirement_document in requirement_documents:
            online_document.add_relyon_requirement(requirement_document)


    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.document_seq:
                instance.created_user = request.user
            instance.updated_user = request.user
            instance.save()
        formset.save_m2m()


    def relyon_requirement_name_link(self, obj):
        relyon_html_link: List[str] = []
        for relyon in obj.relyon_requirement.all():
            document_seq = relyon.document_seq
            document_url = fields.get_reverse_link(
                'admin:document_requirementdocument_change',
                [document_seq]
            )
            html_link = fields.get_html_link(document_url, document_seq)
            relyon_html_link.append(html_link)
        return format_html(', '.join(relyon_html_link))
    

    relyon_requirement_name_link.short_description = _('申請依據 (需求單號)')


edms_admin.register(OnlineDocument, OnlineDocumentAdmin)