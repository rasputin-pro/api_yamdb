from django.urls import include, path
from rest_framework import routers

from api.views import signup_view, token_view, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', signup_view, name="signup"),
    path('v1/auth/token/', token_view, name='token'),
    path('v1/', include(router.urls)),
]
