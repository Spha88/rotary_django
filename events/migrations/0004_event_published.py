# Generated by Django 4.1 on 2022-08-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]