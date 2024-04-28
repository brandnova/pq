from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null = True)
    comment = models.TextField(max_length=500, null = True)
    image = models.ImageField(upload_to='review_images', blank=True, null=True)

    
    def __str__(self):
        return self.name

class Messages(models.Model):
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name
