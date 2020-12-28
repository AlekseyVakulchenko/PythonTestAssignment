from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category
from .utils import save_category


class CategoryView(ModelViewSet):
    """
    Altered ModelViewSet methods create and retrieve to get and create Categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        try:
            save_category(request.data)
        except ValueError:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {'status': ' successful created'},
                status=status.HTTP_201_CREATED
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(
            CategorySerializer(instance).data,
            status=status.HTTP_200_OK
        )
