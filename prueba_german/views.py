from rest_framework import viewsets, permissions

from prueba_german.models import Prueba


class PruebaViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = Prueba.objects.all()