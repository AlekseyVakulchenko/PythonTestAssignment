from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("self",
                               null=True,
                               blank=True,
                               related_name='children',
                               on_delete=models.CASCADE, )
