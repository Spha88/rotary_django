# Generated by Django 4.1 on 2022-08-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_story_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(blank=True, help_text='This field will be auto populated on save', null=True),
        ),
    ]