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
###


from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
#####
from Account.permissios import UserIsAdminMzi
from rest_framework.pagination import PageNumberPagination

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





class CustomPageNumberPagination(PageNumberPagination):
    page_size = 7  # تعداد آیتم‌ها در هر صفحه
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(["POST", "GET", 'DELETE', 'PUT'])
@permission_classes([UserIsAdminMzi])
def admin_ticket(request):
    is_body = bool(request.body)
    if request.method == 'GET' and not is_body:
        data = request.GET
    else:
        data = request.data
    user = request.user
    if request.method == 'GET':
        tickets = Ticket.objects.filter(deleted_at=None, is_ok=True)

        # اعمال صفحه بندی
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(tickets, request)

        serializer = TicketSerializer(result_page, many=True)
        return paginator.get_paginated_response({"message": 'لیست تیکت های دریافتی', 'data': serializer.data})
