from django.shortcuts import render

# Create your views here.
def nike(req):
    return render(req,'index.html')
def blog(req):
    return render(req,'blog.html')
def cart(req):
    return render(req,'cart.html')