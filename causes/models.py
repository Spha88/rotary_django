from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Cause(models.Model):
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    thumb_nail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = tinymce_models.HTMLField(null=True, blank=True, help_text="Excerpt is made from the first paragraph of content") 
    content = tinymce_models.HTMLField()
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('cause_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:99], allow_unicode=True) #make a slug of no more than 100 characters
        super().save(*args, **kwargs)
