# Generated by Django 4.1 on 2022-08-05 17:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]