from rest_framework import serializers
from prueba_german.models import Prueba


class MapsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prueba
        fields = '__all__'