from django.shortcuts import render,get_object_or_404
from .models import Gonderi

def gonderi_list(request):
    Gonderiler =  Gonderi.objects.all()
    return render(request, "EdizBlog/liste.html", {'Posts':Gonderiler})


def post_detay(request,pk):
    post = get_object_or_404(Gonderi,pk=pk)
    return render(request, "EdizBlog/detay.html", {'post':post})