from django.db import models

# Create your models here.


class Page (models.Model):
    type = models.TextField()
    title = models.TextField()
    text = models.TextField()
    author = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

