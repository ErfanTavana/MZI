from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .models import Home
from .serializers import HomeSerializer
from Portfolio.models import Portfolio
from Portfolio.serializers import PortfoliosSerializer
from Certificate.models import Certificate
from Certificate.serializers import CertificateSerializer
from Article.models import Article
from Article.serializers import ArticleSerializer


# Create your views here.

@api_view(["GET"])
def home(request):
    if request.method == 'GET':
        is_body = bool(request.body)
        if request.method == 'GET' and not is_body:
            data = request.GET
        else:
            data = request.data
        user = request.user
        if request.method == 'GET':
            home = Home.objects.first()
            serializer1 = HomeSerializer(home)
            portfolio = Portfolio.objects.filter(is_ok=True, deleted_at=None).order_by('-created_at')[:3]
            serializer2 = PortfoliosSerializer(portfolio, many=True)
            certificate = Certificate.objects.filter(is_ok=True, deleted_at=None).order_by('-created_at')[:3]

            serializer3 = CertificateSerializer(certificate, many=True)
            article = Article.objects.filter(is_ok=True, deleted_at=None).order_by('-created_at')[:3]
            serializer4 = ArticleSerializer(article, many=True)
            return Response({"message": 'اطلاعات صفحه ی اصلی شما',
                             'data': {"info": serializer1.data, 'portfolio': serializer2.data,
                                      'certificate': serializer3.data, 'article': serializer4.data}},
                            status=status.HTTP_200_OK)
