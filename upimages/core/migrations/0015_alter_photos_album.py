# Generated by Django 3.2.3 on 2021-06-01 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210601_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='album',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='core.album'),
        ),
    ]
