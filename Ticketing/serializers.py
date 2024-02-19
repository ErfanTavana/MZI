from rest_framework import serializers
from .models import Ticket
from MZI.serializers import BaseModelSerializer


class TicketSerializer(BaseModelSerializer):
    class Meta:
        model = Ticket
        fields = BaseModelSerializer.Meta.fields + (
            'name',
            'subject',
            'user_type',
            'priority',
            'phone_number',
            'email',
            'additional_description',
        )
