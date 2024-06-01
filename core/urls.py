from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactViewSet,
    InteractionViewSet,
    UserRegistrationViewSet,
    UserLoginViewSet,
    UserProfileViewSet,
)
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r"login", UserLoginViewSet, basename="login")
router.register(r"users", UserRegistrationViewSet, basename="user")
router.register(r"contacts", ContactViewSet, basename="contact")
router.register(r"interactions", InteractionViewSet, basename="interaction")
router.register(r"profile", UserProfileViewSet, basename="profile")


urlpatterns = [
    path("", include(router.urls)),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
