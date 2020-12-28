from .serializers import CreateCategorySerializer


def save_category(obj, parent=None):
    """
    recursive save category
    """
    serializer = CreateCategorySerializer(data={'name': obj.get('name'),
                                                'parent': parent,
                                                'children': []})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    if obj.get('children'):
        for child in obj.get('children'):
            save_category(child, serializer.data.get('id'))
