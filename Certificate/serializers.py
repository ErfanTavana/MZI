
from rest_framework import serializers
from  MZI.serializers import BaseModelSerializer
from .models import Certificate

class CertificateSerializer(BaseModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'id',
            'user',
            'title',
            'image',
        )