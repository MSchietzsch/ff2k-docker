from .models import Story
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

if settings.ENVIRONMENT != "dev":    

    @receiver(post_save, sender=Story)
    def index_post(sender, instance, **kwargs):
        instance.indexing()