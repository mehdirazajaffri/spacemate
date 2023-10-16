from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def all_with_deleted(self):
        return super().get_queryset()

    def deleted(self):
        return super().get_queryset().filter(deleted_at__isnull=False)

    def hard_delete(self):
        return super().get_queryset().filter(deleted_at__isnull=False).delete()

    def restore(self):
        return super().get_queryset().update(deleted_at=None)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    objects = BaseManager()

    class Meta:
        abstract = True
