from django.db import models

# Create your models here.


class Student(models.Model):
    f_name = models.CharField(max_length=50,null=True,blank=True)
    l_name = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return f"{self.f_name} | {self.l_name}"
