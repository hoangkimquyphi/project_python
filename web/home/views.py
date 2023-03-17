from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request,'home.html')
def productDetail(request):
    return render(request,'product_detail.html')
