
from .core import DocumentForm
from ..models.requirement import RequirementDocument

class RequirementDocumentForm(DocumentForm):


    class Meta:
        model = RequirementDocument
        fields = '__all__'