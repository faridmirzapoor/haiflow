from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """سریالایزر کاربر برای نمایش در پروفایل و پاسخ لاگین. نقش از groups گرفته می‌شود."""

    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "groups",
            "status",
            "gender",
            "is_active",
            "date_joined",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields


class LoginSerializer(TokenObtainPairSerializer):
    """لاگین با username و password؛ در پاسخ علاوه بر توکن، اطلاعات کاربر برمی‌گردد."""

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.status != User.Status.ACTIVE:
            raise serializers.ValidationError(
                {"detail": "حساب کاربری شما غیرفعال یا در انتظار تایید است."}
            )
        data["user"] = UserSerializer(user).data
        return data
