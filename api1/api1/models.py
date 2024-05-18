from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
