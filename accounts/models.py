from django.db import models

class Register(models.Model):
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=12)
    password=models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class UserInfo(models.Model):
    fullname=models.CharField(max_length=100)
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    working_choices=[
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    working=models.CharField(max_length=3, choices=working_choices)
    working_hours=models.IntegerField()
    
    def __str__(self):
        return self.fullname
