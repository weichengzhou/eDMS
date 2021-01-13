
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class SuspendableModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_suspend=False)


class SuspendableModel(models.Model):

    is_suspended = models.BooleanField(
        default=False,
        verbose_name='是否停用'
    )

    suspended_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        verbose_name='停用的人員',
        on_delete=models.SET_NULL,
        related_name="%(class)s_suspended_user"
    )


    suspended_datetime = models.DateTimeField(
        default=None,
        null=True,
        verbose_name='停用的時間'
    )


    def delete(self, *args, **kwargs):
        """
        Use `suspend` to replace `delete`.
        Define suspend method.
        """
        self.suspend()


    def suspend(self):
        self.suspended_datetime = timezone.now
    

    class Meta:
        abstract = True