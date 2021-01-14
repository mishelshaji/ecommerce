from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Category Name'
    )

    description = models.TextField(
        max_length=500,
        verbose_name='Description',
    )

    def __str__(self):
        return self.name