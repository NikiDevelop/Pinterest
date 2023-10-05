from django.shortcuts import render
from pinterest.models import Pinterest
from django.db.models import Q

def home(request):
      
    posts = Pinterest.objects.all()
    if "buscar" in request.GET:
        queryset = request.GET.get("buscar")

        if queryset:
            posts = Pinterest.objects.filter(
                Q(titulo__icontains = queryset) 
            
            ).distinct()
    return render(request, "index.html", {"posts": posts})

def explorar(request):
    return render(request, "explorar.html")