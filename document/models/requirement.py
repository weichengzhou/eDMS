
from typing import List

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core import validator
from core.model import TraceableModel, SuspendableModel
from .core import Document


"""
需求單
"""
class RequirementDocument(Document, TraceableModel, SuspendableModel):

    _upload_to_path: str = 'upload/requirement_document/'
    _allowed_extensions: List[str] = ['.doc', 'docx', '.pdf']
    _max_size: int = 25 * 1024 * 1024


    document_seq = models.CharField(
        max_length=30,
        primary_key=True,
        verbose_name='需求單號'
    )


    document = models.FileField(
        upload_to=_upload_to_path,
        verbose_name='需求單',
        help_text=_('檔案格式 (.doc, .docx, .pdf)'),
        validators=[
            validator.FileExtensionValidator(_allowed_extensions),
            validator.FileSizeValidator(_max_size)
        ]
    )


    apply_date = models.DateField(
        default='2021-1-1',
        verbose_name = '申請日期'
    )


    def __str__(self):
        return self.document_seq


    class Meta():
        db_table = 'requirement_document'
        verbose_name = '需求單'
        verbose_name_plural = '需求單'