
from django import forms
from django.conf import settings
from django.utils.html import format_html

class DocumentMultipleChoiceField(forms.ModelMultipleChoiceField):


    def label_from_instance(self, obj):
        return obj.document_seq