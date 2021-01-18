from rest_framework import generics

from .models import EonsSite, EonsCsv
from .serializers import EonsSiteSerializer, EonsCsvSerializer

# EONS Site API views
class EonsSiteList(generics.ListCreateAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer

class EonsSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer

# EONS CSV API vies
class EonsCsvList(generics.ListCreateAPIView):
    queryset = EonsCsv.objects.all()
    serializer_class = EonsCsvSerializer

class EonsCsvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsCsv.objects.all()
    serializer_class = EonsCsvSerializer