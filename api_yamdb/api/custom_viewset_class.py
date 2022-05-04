from rest_framework import mixins, viewsets


class CreateListViewset(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """Class CreateListVewset limits operations
    by creating, destroyng object and getting list of objects
    """
