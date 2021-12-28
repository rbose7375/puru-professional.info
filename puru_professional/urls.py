"""puru_professional URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from puruweb import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main,name="main"),
    path('main.html',views.contact,name='main.html'),
    path('main', views.main,name="main"),
<<<<<<< HEAD
<<<<<<< HEAD
    path('login',views.logi , name="singUpData"),
    path('entrance',views.login , name="entrance"),
    path('entrance/<int:id>/',views.login, name="entrance"),
    path('home',views.home , name="show"),
    path('homes',views.homes , name="homes"),
    path('delete/<int:id>/',views.deleteData , name="deleteData"),
    path('update/<int:id>/',views.update , name="update"),
    path('update.html/',views.home , name="update"),
    path('updat/<int:id>/',views.updat , name="updat"),
    path('personaldetail',views.Personal , name="personaldetail"),
    path('gallarys',views.gallarys , name="gallarys"),
    path('img',views.img , name="img"),    
=======
    path('login',views.logi , name="login"),
    path('entrance',views.login , name="entrance"),
    # path('',views.contact , name="main.html#contact")
>>>>>>> 2155350 (working now long signup contact)
=======
    path('login',views.logi , name="singUpData"),
    path('entrance',views.login , name="entrance"),
    path('entrance/<int:id>/',views.login, name="entrance"),
    path('home',views.home , name="show"),
    path('homes',views.homes , name="homes"),
    path('delete/<int:id>/',views.deleteData , name="deleteData"),
    path('update/<int:id>/',views.update , name="update"),
    path('update.html/',views.home , name="update"),
    path('updat/<int:id>/',views.updat , name="updat"),
    path('personaldetail',views.Personal , name="personaldetail"),
<<<<<<< HEAD
    path('gallary',views.gallary , name="gallary"),
    
>>>>>>> 02329d5 (tatti gallary)
=======
    path('gallarys',views.gallarys , name="gallarys"),
    path('img',views.img , name="img"),    
>>>>>>> 5ab05b1 (almost done)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
