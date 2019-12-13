from django.db import models

# Create your models here.
class Pictionary(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.first_name
    def save_pictionary(self):
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length =70)
    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length =70)
    def __str__(self):
        return self.location_name
    
class Photos(models.Model):
    image = 
    name =
    description = 
    location =
    category =
    photographer =
    
    
    
    