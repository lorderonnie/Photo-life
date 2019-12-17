from django.contrib import admin
from .models import Pictionary,Category,Location,Photos
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('location',)



admin.site.register(Pictionary)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photos)




