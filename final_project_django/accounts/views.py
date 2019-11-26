from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def admin_accounts(request):
    accounts = User.objects.all()
    serializers = UserSerializer(accounts, many=True)
    return Response(serializers.data)

# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(request.user)
#     if user.is_valid():
#         user.save()
#         return Response({message: "회원가입이 완료되었습니다."})
#     return Response(status=400)

# @api_view(['GET'])
# def signout(request):
#     request.user.delete()
#     return Response({message: "회원탈퇴가 완료되었습니다."})

# @api_view(['GET', 'POST'])
# def login(request):
#     if request.user.is_authenticated:
#         return Response({message: "이미 로그인 되어있습니다."})
    
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.POST)
#         if serializer.is_valid():
#             auth_login(request, serializer.get_user())
#     else:
#         serializer = UserSerializer()
#     return Response(serializer.data)

# def logout(request):
#     pass

class UserAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)