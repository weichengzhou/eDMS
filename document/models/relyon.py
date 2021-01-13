

from django.db import models
from django.utils.translation import ugettext_lazy as _


"""
上線申請單需要依據需求單
此為 M對M關係
"""
class OnlineRelyOnRequirement(models.Model):

    online_document = models.ForeignKey(
        'OnlineDocument',
        on_delete=models.CASCADE
    )

    requirement_document = models.ForeignKey(
        'RequirementDocument',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return 'Relyon %s' % self.requirement_document.document_seq


    class Meta:
        db_table = 'online_relyon_requirement'
        verbose_name = '上線依據'
        verbose_name_plural = '上線依據'