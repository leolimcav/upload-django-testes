from .serializers import AlbumSerializer, PhotoSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Album, Photos

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [AllowAny]
    
class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['uuid', 'album']
    ordering_fields = ['description']