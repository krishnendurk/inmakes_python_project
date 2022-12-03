from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('', views.demo2, name='demo2')
    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact')
]
