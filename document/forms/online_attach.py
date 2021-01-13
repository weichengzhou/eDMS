
from .core import DocumentForm
from ..models.online_attach import OnlineAttachment


class OnlineAttachmentForm(DocumentForm):


    class Meta:
        model = OnlineAttachment
        fields = '__all__'