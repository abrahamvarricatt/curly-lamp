
from rest_framework import viewsets
from .models import HouseData
from .serializers import HouseDataSerializer


class HouseDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows houses to be viewed or edited
    """
    queryset = HouseData.objects.all()
    serializer_class = HouseDataSerializer
