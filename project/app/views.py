from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('Django first work')
def second(request,a,b):
    return HttpResponse(a)
def bonus(req,s,y):
    if y>5:
        b=s*5/100
        return HttpResponse(b)
    else:
        return HttpResponse(s)
def divisible(req,n):
    d=n%10
    if d%3==0:
        return HttpResponse('divisible')
    else:
        return HttpResponse('Not')
def ebill(req,u):
    if u<100:
        return HttpResponse(0)
    elif u<200:
        pa=(u-100)*5
        return HttpResponse(pa)
    else:
        pa=(100*5)+(u-200)*10
        return HttpResponse(pa)
def city(req,c):
    if c=='delhi':
        return HttpResponse('red fort')
    elif c=='agra':
        return HttpResponse('Taj Mahal')
    elif c=='jaipur':
        return HttpResponse('Jal Mahal')
def day(req,d):
    if d==1:
        return HttpResponse('sunday')
    elif d==2:
        return HttpResponse('Monday')
    elif d==3:
        return HttpResponse('Thuesday')
    elif d==4:
        return HttpResponse('wensday')
    elif d==5:
        return HttpResponse('thursday')
    elif d==6:
        return HttpResponse('friday')
    elif d==7:
        return HttpResponse('saturday')
def bike(req,p):
    if p>100000:
        t=p*15/100
        return HttpResponse(t)
    elif p>50000 and p<=100000:
        t=p*10/100
        return HttpResponse(t)
    elif p<=50000:
        t=p*5/100
        return HttpResponse(t)