
from .core import DocumentForm
from ..models.checkout import CheckoutDocument


class CheckoutDocumentForm(DocumentForm):


    class Meta:
        model = CheckoutDocument
        fields = '__all__'