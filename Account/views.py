#################################################################
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


################################################################


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user using the provided phone number and password
        user = authenticate(username=username, password=password)

        if user is not None:
            # Delete the existing token, if it exists
            Token.objects.filter(user=user).delete()
            # Create a new token for the authenticated user
            token = Token.objects.create(user=user)
            user.last_login = timezone.now()
            user.is_active = True
            user.save()
            response = Response({'message': 'ok', 'Authorization': f"Token {token.key}"},
                                status=status.HTTP_200_OK)
            # response.set_cookie('Authorization', f"Token {token.key}",
            #                     httponly=True, secure=True)
            return response

        else:
            return Response({'message': 'کاربر وجود ندارد  یا رمز عبور اشتباه است'}, status=status.HTTP_400_BAD_REQUEST)
