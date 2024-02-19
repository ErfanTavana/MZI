from .models import Base_Model
from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base_Model
        fields = (
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
            'deleted_by',
            'is_ok',
            'is_changeable'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
            'deleted_by',
            'is_ok',
            'is_changeable'
        )
