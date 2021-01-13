
import os
from typing import List

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):


    def document_name(self):
        return str(self.document).rsplit('/', 1)[1]

    class Meta:
        abstract = True


class DocumentManager(models.Manager):
    pass