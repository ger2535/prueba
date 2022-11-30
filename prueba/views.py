from rest_framework import viewsets, permissions

from .models import Prueba
from .serializer import PruebaSerializer


class PruebaViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer