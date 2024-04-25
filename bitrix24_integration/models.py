from django.db import models

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class NameWoman(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class NameMan(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
