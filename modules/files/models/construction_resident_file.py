""" Model file image """
# Django
from django.db import models
# Utils model
from modules.utils.models import BaseModel

class ConstructionResidentFile(BaseModel):
    file_doc_img = models.FileField(upload_to='Docs/proyect/construction_resident', null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.file_doc_img)
