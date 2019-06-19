from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)
    description = models.TextField(max_length=400, blank=True)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now=True)
    cover = models.ImageField(blank=True, upload_to='covers/')

    def __str__(self):
        return self.title