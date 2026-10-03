from django.shortcuts import render
from .product_data import sidebar_data
def home(request):
    return render(request,"home.html",{"data":sidebar_data.menu_data})
