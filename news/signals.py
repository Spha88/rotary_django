from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Story
from excerpt_html import excerpt_html

@receiver(pre_save, sender=Story)
def create_excerpt(sender, instance, **kwargs):
    instance.excerpt = excerpt_html(instance.body, 10)