from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)     
    username = models.CharField( max_length=50 , editable=False)
    password = models.CharField(max_length=50 , editable=False)

    def __str__(self):
        return f"{self.name} \n {self.username} \n {self.password}"
    

class Taskadd(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user_task = models.ForeignKey(user , on_delete=models.CASCADE , blank=True , null=True)

    def __str__(self):
        return f"{self.title}"