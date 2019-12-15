from django.db import models

# Create your models here.
class Pictionary(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    def save_pictionary(self):
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length =70)
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos
    
    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length =70)
    def __str__(self):
        return self.location_name
    
class Photos(models.Model):
    image= models.ImageField(upload_to = 'home/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ManyToManyField(Location)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photographer =  models.CharField(max_length =60)
    
    
    