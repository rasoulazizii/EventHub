from django.db import models


class AbstractModel(models.Model):
    id = models.UUIDField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
        