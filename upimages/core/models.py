import uuid
from django.db import models
from django.db.models.fields import UUIDField
from django.db.models.fields.files import FileField, ImageField

# Create your models here.

class Album(models.Model):
  uuid = models.UUIDField(primary_key=True, null=False, blank=False, editable=False, default=uuid.uuid4)
  name = models.TextField(null=False, blank=False)

class Photos(models.Model):
  uuid = models.UUIDField(primary_key=True, null=False, blank=False, editable=False, default=uuid.uuid4)
  description = models.TextField(null=True, blank=True)
  image = ImageField(upload_to='uploads/', blank=True)
  album = models.ForeignKey(Album, editable=True, blank=False, null=False, on_delete=models.CASCADE, related_name='album')