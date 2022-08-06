from datetime import datetime
from django.db import models

from tinymce import models as tinymce_models

class Cause(models.Model):
    title = models.CharField(max_length=150)
    thumb_nail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = tinymce_models.HTMLField(null=True, blank=True, help_text="Excerpt is made from the first paragraph of content") 
    content = tinymce_models.HTMLField()
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
