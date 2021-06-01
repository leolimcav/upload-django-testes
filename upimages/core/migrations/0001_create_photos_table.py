# Generated by Django 3.2.3 on 2021-06-01 01:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('4b7c3a9a-6f5b-4a44-aba9-d0fc637e8f15'), primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]