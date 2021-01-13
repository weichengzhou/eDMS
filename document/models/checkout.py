
from typing import List

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core import validator
from core.model import TraceableModel, SuspendableModel
from .core import Document
from ..models.requirement import RequirementDocument


"""
Checkout單
"""
class CheckoutDocument(Document, TraceableModel, SuspendableModel):

    _upload_to_path: str = 'upload/checkout_document'
    _allowed_extensions: List[str] = ['.doc', '.docx', '.pdf']
    _max_size: int = 25 * 1024 * 1024


    document_seq = models.AutoField(
        primary_key=True,
        verbose_name='文件編號'
    )


    document = models.FileField(
        upload_to=_upload_to_path,
        verbose_name='Checkout申請單',
        help_text='檔案格式 (.doc, .docx, .pdf)',
        validators=[
            validator.FileExtensionValidator(_allowed_extensions),
            validator.FileSizeValidator(_max_size)
        ]
    )


    relyon_requirement = models.ForeignKey(
        'RequirementDocument',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='申請依據',
        help_text='需求單單號'
    )


    apply_date = models.DateField(
        default='2021-1-1',
        verbose_name = '申請日期'
    )


    def __str__(self):
        return str(self.document_seq)
    

    class Meta:
        db_table = 'checkout_document'
        verbose_name = 'Checkout申請單'
        verbose_name_plural = 'Checkout申請單'