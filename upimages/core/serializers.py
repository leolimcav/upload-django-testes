from django.db.models.fields import UUIDField
from rest_framework import serializers
from .models import Album, Photos

class AlbumRelatedSerializer(serializers.PrimaryKeyRelatedField):
  def display_value(self, instance):
      return 'Album: Nome: {} ID: {} '.format(instance.name, instance.uuid)
      
class AlbumSerializer(serializers.ModelSerializer):
  album = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Album
    fields = '__all__'
    depth = 1

class PhotoSerializer(serializers.ModelSerializer):
  album = AlbumRelatedSerializer(many=False, allow_null=False, queryset=Album.objects.all())
  class Meta:
    model = Photos
    fields = '__all__'
    depth = 1

