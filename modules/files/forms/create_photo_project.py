""" project create photo form"""
# Django
from django import forms
# Models
from modules.project.models import Project
from modules.files.models import ImageProject

class ImageProjectCreate(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = ImageProject
        fields = ['image',]
    

    def save(self, *args, **kwargs):
        import pdb; pdb.set_trace()
