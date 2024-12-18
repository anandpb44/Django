"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),
    path('second/<int:a>/<int:b>',views.second),
    path('bonus/<int:s>/<int:y>',views.bonus),
    path('divisible/<int:n>',views.divisible),
    path('ebill/<int:u>',views.ebill),
    path('city/<c>',views.city),
    path('day/<int:d>',views.day),
    path('bike/<int:p>',views.bike),
    path('con',views.html),
    path('table',views.age),
    path('add',views.add),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.del_std),
]
