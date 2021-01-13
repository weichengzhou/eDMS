
from django.forms import ModelForm

from ..models.core import Document

class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = '__all__'