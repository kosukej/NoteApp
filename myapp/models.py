import uuid
from django.db import models
from django.utils import timezone


# Create your models here.
class NoteTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="見出し", max_length=100)
    text = models.TextField(verbose_name="本文", max_length=400)
    created_at = models.DateTimeField(verbose_name="作成日付", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="編集日付", blank=True, null=True)
