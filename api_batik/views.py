from rest_framework import viewsets
from .models import KainBatik
from .serializers import KainBatikSerializer

class KainBatikViewSet(viewsets.ModelViewSet):
    queryset = KainBatik.objects.all()
    serializer_class = KainBatikSerializer