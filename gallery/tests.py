from django.test import TestCase
from .models import Photos,Category,Location,Pictionary


#creating a method

class Pictionary(TestCase):
    def setUp(self):
        self.ronnie= Pictionary(first_name = 'ronnie',last_name='Mwambia')
    def test_instance(self):
        self.assertTrue(isinstance(self.ronnie,Pictionary))

#creating picture function

class Photos(TestCase):
    #creating a information bar(Pictionary)and saving it
    def setUp(self):
        self.ronnie= Pictionary(first_name = 'ronnie',last_name='Mwambia')
        self.ronnie.save_pictionary

    #creating a new category and saving it
        self.new_category = Category (name= 'testing')
        self.new_category.save_category()
    
    
    
    
    
    
    
