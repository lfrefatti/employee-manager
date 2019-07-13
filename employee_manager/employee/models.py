from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
