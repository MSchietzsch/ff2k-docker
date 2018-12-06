from django.db import models

# Create your models here.

class Credentials(models.Model):
    cred = models.TextField(blank=False, db_index=False)
