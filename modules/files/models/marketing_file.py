""" Model Marketing """
# Django
from django.db import models
# Utils model
from modules.utils.models import BaseModel

class MarketingFile(BaseModel):
    file_doc_img = models.FileField(upload_to='Docs/proyect/marketing', null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.file_doc_img)
