from django.shortcuts import render
from .models import Category,Image

def home(request):
    images=Image.objects.all()
    cats=Category.objects.all()
    data={
        'images':images,
        'cats':cats
    }
    return render(request,'home.html',data)


def category(request,cid):
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    data={
        'images':images,
        'cats':cats
    }
    return render(request,'home.html',data)
