from django.shortcuts import render
from .models import Gonderi

def gonderi_list(request):
    Gonderiler =  Gonderi.objects.all()
    return render(request, "EdizBlog/liste.html", {'Posts':Gonderiler})
