from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
# from django.db.models import Avg, F

from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination, \
    PageNumberPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly, AllowAny)
from rest_framework.response import Response
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken


from api.serializers import (SignUpSerializer, TokenSerializer,
                             UserSerializer, ProfileSerializer,
                             CategorySerializer, GenreSerializer,
                             TitleReadSerializer, TitleWriteSerializer)
from api.permissions import IsAdmin, IsAdminOrReadOnly
from reviews.models import User, Category, Genre, Title

from api.custom_viewset_class import CreateListViewset
from api.filters import TitleFilter


@api_view(['POST'])
def signup_view(request):
    """Create user with unique username and email.
    Send confirmation code to user email.
    """
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_confirmation_code(user)
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


def send_confirmation_code(user):
    """Sending confirmation code to user email."""
    confirmation_code = default_token_generator.make_token(user)
    subject = 'Код подтверждения'
    message = f'confirmation_code: {confirmation_code}'
    return send_mail(subject, message, None, (user.email, ))


@api_view(['POST'])
def token_view(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        user = get_object_or_404(User, username=username)
        confirmation_code = serializer.data['confirmation_code']
        if default_token_generator.check_token(user, confirmation_code):
            refresh = RefreshToken.for_user(user)
            return Response(
                {'access': str(refresh.access_token)}, status=HTTP_200_OK
            )
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, )
    ordering = ('username', )
    filter_backends = (SearchFilter, )
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    lookup_value_regex = r'[\w\@\.\+\-]+'
    search_fields = ('username', )

    @action(
        detail=False, methods=['get', 'patch'],
        url_path='me', url_name='me',
        permission_classes=(IsAuthenticated, )
    )
    def about_me(self, request):
        serializer = ProfileSerializer(request.user)
        if request.method == 'PATCH':
            serializer = ProfileSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.data, status=HTTP_200_OK)


class CategoryViewSet(CreateListViewset):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )
    filter_backends = [SearchFilter]
    lookup_field = 'slug'
    search_fields = ('=name',)


class GenreViewSet(CreateListViewset):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly, )
    filter_backends = [SearchFilter]
    lookup_field = 'slug'
    search_fields = ('=name',)


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.annotate()
    # rating=Avg(F('reviews__score'))

    permission_classes = (IsAdminOrReadOnly, )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
