from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import people


# Create your views here.
def demo(request):
    obj = place.objects.all()
    ob = people.objects.all()
    # name="india"
    return render(request, "index.html", {'result': obj,'resu': ob})


# # def demo2(request):
#     ob = people.objects.all()
#     return render(request, "index.html", {'resu': ob})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result':res,'sub1':res2,'mul1':res3,'div1':res4})
