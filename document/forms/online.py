
from django import forms
from django.utils.translation import ugettext_lazy as _

from core.field import DocumentMultipleChoiceField
from .core import DocumentForm
from ..models.online import OnlineDocument
from ..models.requirement import RequirementDocument

class OnlineDocumentForm(DocumentForm):

    relyon = DocumentMultipleChoiceField(
        queryset=RequirementDocument.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label='申請依據',
        help_text=_('需求單號 (按住Ctrl可複選)')
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.initialize_relyon(kwargs['instance'])
        
        
    def initialize_relyon(self, instance):
        if instance is None:
            return
        self.fields['relyon'].initial = \
            instance.get_relyon_requirement_seq()
            

    class Meta:
        model = OnlineDocument
        fields = '__all__'