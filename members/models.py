from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

TITLE_CHOICES = [
    ('Mr.', 'Mr'),
    ('Mrs.', 'Mrs'),
    ('Miss.', 'Miss'),
    ('Dr.', 'Dr'),
    ('Prof.', 'Professor'),
    ('Adv.', 'Advocate'),

]

class Member(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rotary_position = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True, help_text="e.g Retired teacher, electrician, physiotherapist etc.")
    profile_picture = models.ImageField(upload_to='members/%Y/%m/%d/')
    bio = tinymce_models.HTMLField(blank=True, null=True)
    active = models.BooleanField(default=False, help_text="Tick if the members is still active in rotary")
    registration_date = models.DateField(help_text="The date the member acquired membership")
    resignation_date = models.DateField(blank=True, null=True, help_text="If member is not active the date on which he/she retired can be indicated here")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}" 

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}", allow_unicode=True)
        super().save(*args, **kwargs)



