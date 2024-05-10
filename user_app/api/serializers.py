from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        username = self.validated_data.get("username")
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        confirm_password = self.validated_data.get("confirm_password")

        if not all([username, password, email, confirm_password]):
            raise serializers.ValidationError({"error": "All fields are required."})

        if password != confirm_password:
            raise serializers.ValidationError({"error": "Passwords do not match."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"error": "User with this email already exists."}
            )

        account = User(username=username, email=email, password=password)
        account.set_password(password)
        account.save()

        return account
