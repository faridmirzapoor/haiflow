from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import LoginSerializer, UserSerializer


class LoginView(TokenObtainPairView):
    """
    لاگین با username و password.
    پاسخ: access, refresh و user.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class RefreshTokenView(TokenRefreshView):
    """دریافت access token جدید با refresh token."""
    permission_classes = (AllowAny,)


class LogoutView(TokenBlacklistView):
    """خروج: رفرش توکن در بلاک‌لیست قرار می‌گیرد. بدنه: {"refresh": "..."}"""
    permission_classes = (AllowAny,)


class MeView(APIView):
    """اطلاعات کاربر لاگین‌شده."""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserListView(APIView):
    """لیست کاربران (برای انتخاب در ابلاغیه و وظایف)."""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        from .models import User
        users = User.objects.filter(is_active=True).order_by("first_name", "last_name")
        return Response(UserSerializer(users, many=True).data)


