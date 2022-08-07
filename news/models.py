from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Story(models.Model):
    slug = models.SlugField(blank=True, null=True, help_text="This field will be auto populated on save")
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='news/%Y/%m/%d/')
    excerpt = tinymce_models.HTMLField(blank=True, null=True)
    body = tinymce_models.HTMLField()
    author = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)