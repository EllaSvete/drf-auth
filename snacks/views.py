from rest_framework import generics
from .models import Snack
from .permissions import IsPurchaserOrReadOnly
from .serializers import SnackSerializer

# Create your views here.
class SnackList(generics.ListCreateAPIView):

  queryset = Snack.objects.all()
  serializer_class = SnackSerializer


class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsPurchaserOrReadOnly,)
  queryset = Snack.objects.all()
  serializer_class = SnackSerializer