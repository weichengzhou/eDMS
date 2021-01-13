
from typing import List, Iterable

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core import validator
from core.model import TraceableModel, SuspendableModel
from .core import Document, DocumentManager
from .requirement import RequirementDocument
from .relyon import OnlineRelyOnRequirement


"""
上線申請單
"""
class OnlineDocument(Document, TraceableModel, SuspendableModel):
    
    _upload_to_path: str = 'upload/online_document/'
    _allowed_extensions: List[str] = ['.doc', '.docx', '.pdf']
    _max_size: int = 25 * 1024 * 1024


    document_seq = models.CharField(
        max_length=30,
        primary_key=True,
        verbose_name='上線申請單編號'
    )


    document = models.FileField(
        upload_to=_upload_to_path,
        verbose_name='上線申請單',
        help_text=_('檔案格式 (.doc, .docx, .pdf)'),
        validators=[
            validator.FileExtensionValidator(_allowed_extensions),
            validator.FileSizeValidator(_max_size)
        ]
    )


    """
    對應到 RequirementDocument
    透過 OnlineRelyOnRequirement 表格
    online_document 表示 F.K. 到此表格 (OnlineDocument) 的欄位
    requirement_document 表示 F.K. 到表格 RequirementDocument 的欄位
    """
    relyon_requirement = models.ManyToManyField(
        'RequirementDocument',
        through='OnlineRelyOnRequirement',
        through_fields=('online_document', 'requirement_document')
    )


    apply_date = models.DateField(
        default='2021-1-1',
        verbose_name = '申請日期'
    )


    def __str__(self):
        return self.document_seq


    def clear_relyon_requirement(self):
        self.relyon_requirement.clear()


    def add_relyon_requirement(self, relyon_requirement: RequirementDocument):
        self.relyon_requirement.add(relyon_requirement)


    def get_relyon_requirement_seq(self) -> List[int]:
        relyon_requirments: List[RequirementDocument] = []
        for relyon in self.relyon_requirement.all():
            relyon_requirments.append(relyon.document_seq)
        return relyon_requirments


    class Meta():
        db_table = 'online_document'
        verbose_name = '上線申請單'
        verbose_name_plural = '上線申請單'