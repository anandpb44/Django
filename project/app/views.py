from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('Django first work')
def second(request,a,b):
    return HttpResponse(a,b)