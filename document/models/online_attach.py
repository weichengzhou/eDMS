
from typing import List

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core import validator
from core.model import TraceableModel, SuspendableModel
from .core import Document
from .online import OnlineDocument

"""
上線申請單附件
"""
class OnlineAttachment(Document, TraceableModel, SuspendableModel):

    _upload_to_path: str = 'upload/online_attachment'
    _allowed_extensions: List[str] = ['.doc', '.docx', '.pdf']
    _max_size: int = 25 * 1024 * 1024

    document_seq = models.AutoField(
        primary_key=True,    
        verbose_name='文件編號'
    )

    document_type = models.CharField(
        max_length=30,
        verbose_name='附件種類'
    )

    document = models.FileField(
        upload_to=_upload_to_path,
        verbose_name='上線申請附件',
        help_text=_('檔案格式 (.doc, .docx, .pdf)'),
        validators=[
            validator.FileExtensionValidator(_allowed_extensions),
            validator.FileSizeValidator(_max_size)
        ]
    )


    attachto_online = models.ForeignKey(
        OnlineDocument,
        verbose_name='上線申請單',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return str(self.document_name())
    

    class Meta():
        db_table = 'online_attachment'
        verbose_name = '上線申請單附件'
        verbose_name_plural = '上線申請單附件'