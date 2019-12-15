from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category


# Create your views here.
def gallery(request):
    return render(request,'gallery/home.html')


def search_results(request):
    
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"category": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
   






