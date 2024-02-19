#################################################################
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from django.utils import timezone
################################################################
from .serializers import TicketSerializer
from .models import Ticket

@api_view(["POST"])
def ticket(request):
    data = request.data
    method = request.method
    if request.method == 'POST':
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'تیکت با موفقیت ثبت شد', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'خطا در اطلاعات ارسال شده ', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)