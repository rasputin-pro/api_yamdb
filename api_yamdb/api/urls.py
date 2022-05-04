from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, GenreViewSet, signup_view,
                       TitleViewSet, token_view, UserViewSet)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'titles', TitleViewSet, basename='title')

urlpatterns = [
    path('v1/auth/signup/', signup_view, name="signup"),
    path('v1/auth/token/', token_view, name='token'),
    path('v1/', include(router.urls)),
]
