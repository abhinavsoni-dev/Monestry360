from django.db import models

class ArchiveDummy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
