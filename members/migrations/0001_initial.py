# Generated by Django 4.1 on 2022-08-06 13:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(choices=[('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Miss.', 'Miss'), ('Dr.', 'Dr'), ('Prof.', 'Professor'), ('Adv.', 'Advocate')], max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('rotary_position', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, help_text='e.g Retired teacher, electrician, physiotherapist etc.', max_length=100, null=True)),
                ('profile_picture', models.ImageField(upload_to='members/%Y/%m/%d/')),
                ('bio', tinymce.models.HTMLField(blank=True, null=True)),
                ('active', models.BooleanField(default=False, help_text='Tick if the members is still active in rotary')),
                ('registration_date', models.DateField(help_text='The date the member acquired membership')),
                ('resignation_date', models.DateField(blank=True, help_text='If member is not active the date on which he/she retired can be indicated here', null=True)),
            ],
        ),
    ]
