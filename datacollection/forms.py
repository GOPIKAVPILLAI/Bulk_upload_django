from django import forms
# forms.py
from django import forms
# forms.py
from . models import UserFile
from multiupload.fields import MultiFileField

class ImageUploadForm(forms.Form):
    images = MultiFileField( max_num=100, min_num=1)
class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'image']
        widgets = {
            'image': forms.HiddenInput()
        }
