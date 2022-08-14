from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Event(models.Model):
    slug = models.SlugField(blank=True, null=True) # excluded by the EventAdmin model, so it won't appear in the admin site
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='events/%Y/%m/%d/')
    description = tinymce_models.HTMLField()
    date = models.DateTimeField(default=datetime.now, help_text="Date and time the event will start")
    added_by = models.CharField(max_length=200)
    
    venue = models.CharField(max_length=200)
    street = models.CharField(max_length=300)
    suburb = models.CharField(max_length=300, blank=True, null=True)
    town = models.CharField(max_length=300, blank=True, null=True)
    postal_code = models.CharField(max_length=5)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    

