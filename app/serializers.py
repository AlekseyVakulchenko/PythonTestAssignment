from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Category
from .serializers_utils import get_parents


class CategoryNameSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(ModelSerializer):
    parent = SerializerMethodField()
    children = CategoryNameSerializer(many=True)
    siblings = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'children', 'parent', 'siblings']

    def get_parent(self, obj):
        if obj.parent is not None:
            parents = get_parents(obj, parents=[])
            return CategoryNameSerializer(parents, many=True).data or None

    def get_siblings(self, obj):
        if obj.parent is not None:
            siblings_queryset = (Category.objects.filter(parent=obj.parent)
                                                 .exclude(pk=obj.id))
            return CategoryNameSerializer(siblings_queryset,
                                          many=True).data or None


class CreateCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
