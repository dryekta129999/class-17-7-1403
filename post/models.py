from django.db import models

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (

        ('Published', 'Published'),
        ('Unpublished', 'Unpublished'),
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),

    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Published')


    def __str__(self):

        return self.status








