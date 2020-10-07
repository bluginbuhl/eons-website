from rest_framework import generics

from .models import EonsSite
from .serializers import EonsSiteSerializer


class EonsSiteList(generics.ListCreateAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer


class EonsSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer