from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here. What we want to save to database

#django already has everything built in

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #dont want to execute now
    #can use (auto_now_add=True to keep date if dont want to change)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # double underscore method, tells what we want to be returned when calling 
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-home', kwargs={'pk': self.pk})


