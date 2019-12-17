from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Category,Photos


# Create your views here.
def gallery(request):
    photos=Photos.all_photos()
    return render(request,'gallery/home.html',{"photos":photos})


def search_results(request):
    
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = Photos.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
 




