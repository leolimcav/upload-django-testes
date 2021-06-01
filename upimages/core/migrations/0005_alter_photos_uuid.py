# Generated by Django 3.2.3 on 2021-06-01 02:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_photos_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1d98b71a-d349-4d8c-8f45-55f60b0c4eed'), editable=False, primary_key=True, serialize=False),
        ),
    ]
