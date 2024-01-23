from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    online = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}{self.email}{self.online}"