from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
#####
from .serializers import PortfoliosSerializer, CategoryArticleSerializer, TagArticleSerializer
from .models import CategoryArticle, TagArticle, Portfolio
from Account.permissios import UserIsAdminMzi


@api_view(["POST", "GET", 'DELETE', 'PUT'])
@permission_classes([UserIsAdminMzi])
def admin_portfolio(request):
    is_body = bool(request.body)
    if request.method == 'GET' and not is_body:
        data = request.GET
    else:
        data = request.data
    user = request.user
    if request.method == "GET":
        article = Portfolio.objects.filter(is_ok=True, deleted_at=None)
        serializer = PortfoliosSerializer(article, many=True)
        return Response({"message": 'لیست نمونه کار های شما', 'data': serializer.data}, status=status.HTTP_200_OK)
    if request.method == "POST":
        categories_list = []
        hashtags_list = []

        categories = data.get('categories')
        hashtags = data.get('hashtags')
        for category in categories:
            name = category['name']
            try:
                category_article, created = CategoryArticle.objects.get_or_create(name=name)
                categories_list.append(category_article.id)
            except Exception as s:
                print(s)
                continue
        for hashtag in hashtags:
            try:
                name = hashtag['name']
                tag_article, created = TagArticle.objects.get_or_create(name=name)
                hashtags_list.append(tag_article.id)
            except Exception as e:
                print(e)
                continue
        data['user'] = user.id
        data['tags'] = hashtags_list
        data['categories'] = categories_list
        serializer = PortfoliosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": 'نمونه کار با موفقیت ثبت شد', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": 'خطا در مقادیر ارسالی', 'data': serializer.errors})
    if request.method == "DELETE":
        article_id = data.get('article_id')
        try:
            article = Portfolio.objects.get(id=article_id, deleted_at=None, deleted_by=None)
            article.soft_delete(deleted_by=user)
            return Response({'message': 'نمونه کار با موفقیت حذف شد'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": 'نمونه کار مورد نظر یافت نشد'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        article_id = data.get('article_id')
        categories_list = []
        hashtags_list = []

        categories = data.get('categories')
        hashtags = data.get('hashtags')
        for category in categories:
            name = category['name']
            try:
                category_article, created = CategoryArticle.objects.get_or_create(name=name)
                categories_list.append(category_article.id)
            except Exception as s:
                print(s)
                continue
        for hashtag in hashtags:
            try:
                name = hashtag['name']
                tag_article, created = TagArticle.objects.get_or_create(name=name)
                hashtags_list.append(tag_article.id)
            except Exception as e:
                print(e)
                continue
        data['user'] = user.id
        data['tags'] = hashtags_list
        data['categories'] = categories_list
        try:
            article = Portfolio.objects.get(id=article_id, is_ok=True, is_changeable=True, deleted_at=None,
                                            deleted_by=None)
        except Exception as e:
            print(e)
            return Response({"message": 'نمونه کار مورد نظر یافت نشد'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PortfoliosSerializer(instance=article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": 'نمونه کار با موفقیت اپدیت شد', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": 'خطا در مقادیر ارسالی', 'data': serializer.errors})
