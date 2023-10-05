"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('approveuser/home',views.home,name='home2'),
    path('investorsignup',views.investorsignup,name='investorsignup'),
    path('ownersignup',views.ownersignup,name='ownersignup'),
    path('ownersignupaction',views.ownersignupaction,name='ownersignupaction'),
    path('investorsignupaction',views.investorsignupaction,name='investorsignupaction'),
    path('',views.login,name='login'),
    #path('',views.index,name='index'),
    path('loginaction',views.loginaction,name='loginaction'),
    path('logout',views.custom_logout,name='custom_logout'),
    path('approveuser/logout',views.custom_logout,name='custom_logout1'),
    path('approveproject/<int:projectid>',views.approveproject,name='approveproject'),
    path('updatelogin/<int:id>',views.updatelogin,name='updatelogin'),
    path('deletelogin/<int:id>',views.deletelogin,name='deletelogin'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('validateinvestor',views.validateinvestor,name='validateinvestor'),
    path('validateowner',views.validateowner,name='validateowner'),
    path('approveinvestor/<str:username>',views.approveinvestor,name='approveinvestor'),
    path('rejectinvestor/<str:username>',views.rejectinvestor,name='rejectinvestor'),
    path('approveowner/<str:username>',views.approveowner,name='approveowner'),
    path('rejectowner/<str:username>',views.rejectowner,name='rejectowner'),
    path('projectpublish',views.projectpublish,name='projectpublish'),
    path('projectpublishaction',views.projectpublishaction,name='projectpublishaction'),
    path('viewprojects',views.viewprojects,name='viewprojects'),
    path('responseview',views.responseview,name='responseview'),
    path('sendgmail',views.sendgmail,name='sendgmail'),
    path('respond/<int:id>',views.respond,name='respond'),
    path('respondaction',views.respondaction,name='respondaction'),
    path('editusers',views.editusers,name='editusers'),
    path('feedback',views.feedback,name='feedback'),
    path('feedbackaction',views.feedbackaction,name='feedbackaction'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
     path('report',views.report,name='report'),
]
