from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = (
            'id',
            'country',
            'province',
            'city',
            'address',
            'full_address',
            'phone_prefix',
            'phone_number',
            'email',
            'working_days',
            'whatsapp_mz',
            'linkedin_mz',
            'instagram_mz',
            'telegram_mz',
            'vichat_mz',
        )
