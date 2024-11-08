from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

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
def html(req):
    # a='Django'
    # b=['python','php','java']
    # c=4537
    # d=('python','php','java')
    # e={'name':'anu','age':20,'gender':'female'}
    # return render(req,'index.html',{'a':a,'b':b,'c':c,'d':d,'e':e})
    l=[1,2,3,4,5,6]
    u=[{'name':'anu','age':20},{'name':'akhil','age':22},{'name':'deepu','age':20}]
    return render(req,'index.html',{'l':l,'u':u})
def age(req):
    t=[{'name':'anand','age':20},{'name':'akhil','age':32},{'name':'Deepu','age':33},{'name':'Hakkeem','age':25},{'name':'Dijin','age':30},{'name':'sanal','age':31},{'name':'Nabeel','age':29}]
    l1=[]
    l2=[]
    for i in t:
        if i['age']>30:
            l1.append(i)
        else:
            l2.append(i)
    return render(req,'age.html',{'t':t,'l1':l1,'l2':l2})
# std=[]
# def add(req):
#     if req.method=='POST':
#         roll=req.POST['rollno']
#         name=req.POST['name']
#         age=req.POST['age']
#         std.append({'rollno':roll,'name':name,'age':age})
#         print(std)
#         return redirect(add)
#     else:
#         return render(req,'add_std.html',{'std':std})

# def edit(req,no):
#     student=''
#     for i in std:
#         if i['rollno']==no:
#             student=i
#     print(student)
#     if req.method=='POST':
#         roll=req.POST['rollno']
#         name=req.POST['name']
#         age=req.POST['age']
#         student['rollno']=roll
#         student['name']=name
#         student['age']=age
#         return redirect(add)
#     else:
#         return render(req,'edit.html',{'data':student})

# def del_std(req,no):
#     for i in std:
#         if i['rollno']==no:
#             std.remove(i)
#     return redirect(add)
def add(req):
    if req.method=='POST':
        roll=req.POST['rollno']
        name=req.POST['name']
        age=req.POST['age']
        data=Student.objects.create(roll_no=roll,name=name,age=age)
        data.save()
        # std.append({'rollno':roll,'name':name,'age':age})
        # print(std)
        return redirect(add)
    else:
        data=Student.objects.all()
        return render(req,'add_std.html',{'std':data})
    
def edit(req,id):
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['rollno']
        name=req.POST['name']
        age=req.POST['age']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age)
        return redirect(add)
    else:
        return render(req,'edit.html',{'data':data})
def del_std(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(add)

