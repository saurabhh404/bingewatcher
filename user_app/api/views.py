from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializer

# from user_app import models
# from rest_framework.authtoken.models import Token


@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            refresh = RefreshToken.for_user(account)
            response = {
                "success": True,
                "message": "User created successfully",
                "token": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                "username": serializer.data["username"],
                "email": serializer.data["email"],
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
