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
    
    def __str__(self):
        return self.category_name
    
    def get_category(self,cls):
        categories = cls.objects.all()
        return categories
    
    def save_category(self):
        self.save()
        
class Location(models.Model):
    location_name = models.CharField(max_length =70)
    def __str__(self):
        return self.location_name
    
    def get_location(self,cls):
        locations = cls.objects.all()
        return locations
    
    def save_location(self):
        self.save()
        
class Photos(models.Model):
    image= models.ImageField(upload_to ='home/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location =  models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos
    
    @classmethod
    def all_photos(cls):
        photos = cls.objects.all()
        return photos
    
    def save_photo(self):
        self.save()
        
        
    