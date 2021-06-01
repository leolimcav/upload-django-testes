# Generated by Django 3.2.3 on 2021-06-01 02:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210601_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('34acfd97-6afd-40b3-9b78-e8e387e54ae3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
