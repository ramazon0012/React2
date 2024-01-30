from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.name