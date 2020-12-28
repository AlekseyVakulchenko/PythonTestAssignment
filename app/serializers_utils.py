from .models import Category


def get_parents(instance, parents):
    """
    recursive obtain parents by id first parent
    """
    if instance.parent:
        current_parent = Category.objects.get(pk=instance.parent.id)
        parents.append(current_parent)
        get_parents(current_parent, parents)
    return parents
