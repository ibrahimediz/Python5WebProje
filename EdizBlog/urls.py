from django.urls import path
from . import views


urlpatterns = [
    path('', views.gonderi_list, name='gonder_list'),
    path('post/<int:pk>/', views.post_detay, name='post_detay'),
]