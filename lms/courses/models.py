from django.db import models

# Create your models here.
from django.contrib.auth.models import  User
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title