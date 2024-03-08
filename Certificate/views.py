from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
#####
from .serializers import CertificateSerializer
from Account.permissios import UserIsAdminMzi
from .models import Certificate
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 7  # تعداد آیتم‌ها در هر صفحه
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(["POST", "GET", 'DELETE', 'PUT'])
@permission_classes([UserIsAdminMzi])
def admin_certificate(request):
    is_body = bool(request.body)
    if request.method == 'GET' and not is_body:
        data = request.GET
    else:
        data = request.data
    user = request.user
    if request.method == 'GET':
        certificate = Certificate.objects.filter(deleted_at=None, is_ok=True)

        # اعمال صفحه بندی
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(certificate, request)

        serializer = CertificateSerializer(result_page, many=True)
        return paginator.get_paginated_response({"message": 'لیست مدارک شما', 'data': serializer.data})
    if request.method == 'POST':
        data['user'] = user.id
        serializer = CertificateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": 'مدرک با موفقیت ثبت شد', 'data': ''}, status=status.HTTP_200_OK)
        else:
            return Response({"message": 'خطا در مقادیر ارسالی', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        certificate_id = data.get('certificate_id')
        try:
            certificate = Certificate.objects.get(deleted_at=None, is_ok=True, id=certificate_id)
            serializer = CertificateSerializer(instance=certificate, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": 'مدرک با موفقیت اپدیت شد', 'data': serializer.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": 'خطا در مقادیر ارسالی', 'data': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": 'شناسه مدرک اشتباه است', 'data': ''}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        certificate_id = data.get('certificate_id')
        try:
            certificate = Certificate.objects.get(deleted_at=None, is_ok=True, id=certificate_id)
            certificate.soft_delete(deleted_by=user)
            return Response({"message": 'مدرک با موفقیت حذف شد', 'data': ''},
                            status=status.HTTP_200_OK)
        except:
            return Response({"message": 'شناسه مدرک اشتباه است', 'data': ''}, status=status.HTTP_400_BAD_REQUEST)
class CertificatePagination(PageNumberPagination):
    page_size = 9  # تعداد آیتم‌ها در هر صفحه
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(["GET"])
@permission_classes([UserIsAdminMzi])
def certificate(request):
    is_body = bool(request.body)
    if request.method == 'GET' and not is_body:
        data = request.GET
    else:
        data = request.data
    user = request.user
    if request.method == 'GET':
        certificate_id = data.get('certificate_id', None)
        if certificate_id != None:
            try:
                certificate = Certificate.objects.get(id=certificate_id, is_ok=True, is_changeable=True)
                serializer = CertificateSerializer(certificate)
                return Response({"message": 'جزئیات مدرک یا گواهی', 'data': serializer.data})
            except:
                return Response({"message": 'مدرک یا گواهی  با این شناسه یافت نشد', 'data': ''},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            certificate = Certificate.objects.filter(deleted_at=None, is_ok=True)

            # اعمال صفحه بندی
            paginator = CertificatePagination()
            result_page = paginator.paginate_queryset(certificate, request)

            serializer = CertificateSerializer(result_page, many=True)
            return paginator.get_paginated_response({"message": 'لیست مدارک شما', 'data': serializer.data})
