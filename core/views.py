from rest_framework import viewsets
from .models import Contact, Interaction, User
from .serializers import (
    ContactSerializer,
    InteractionSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .helpers import get_tokens_for_user


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "success": True,
                "user": serializer.data,
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class UserLoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.data["email"])
        tokens = get_tokens_for_user(user)
        return Response(
            {
                "success": True,
                "user": UserRegistrationSerializer(user).data,
                "tokens": tokens,
            },
            status=status.HTTP_200_OK,
        )


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            status=status.HTTP_200_OK,
        )


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InteractionViewSet(viewsets.ModelViewSet):
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(contact__user=self.request.user)
