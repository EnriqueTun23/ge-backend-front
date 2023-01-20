""" Model file image """
# Django
from django.db import models
# Utils model
from modules.utils.models import BaseModel

class ImageProject(BaseModel):
    # image = models.ImageField(upload_to='Media/proyect/imagenes', null=True, blank=True)
    image = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('image',)

    def __str__(self):
        return str(self.image)