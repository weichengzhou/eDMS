
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class TraceableModel(models.Model):

    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        verbose_name='新增的人員',
        on_delete=models.PROTECT,
        related_name="%(class)s_created_user"
    )


    created_datetime = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='新增的時間'
    )


    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='最近修改的人員',
        on_delete=models.PROTECT,
        related_name="%(class)s_updated_user"
    )


    updated_datetime = models.DateTimeField(
        verbose_name='最近修改的時間'
    )


    def save(self, *args, **kwargs):
        self.updated_datetime = timezone.now()
        return super().save(*args, **kwargs)


    class Meta:
        abstract = True