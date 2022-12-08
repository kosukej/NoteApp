# Generated by Django 4.1 on 2022-11-18 10:04

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='見出し')),
                ('text', models.TextField(max_length=400, verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日付')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='編集日付')),
            ],
        ),
    ]
