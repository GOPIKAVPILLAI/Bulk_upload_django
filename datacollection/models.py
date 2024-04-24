from django.db import models

# Create your models here.
from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/',)
    # Other fields if needed
class UserFile(models.Model):
    file = models.FileField(upload_to='user_files/')
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE, related_name='user_files', null=True, blank=True)