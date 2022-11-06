from django.contrib import admin
from django.urls import path
from .import  views

app_name = "iha"


urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addiha/',views.addIha,name="addiha"),
    path('iha/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateIha,name="update"),
    path('delete/<int:id>',views.deleteIha,name="delete"),
    path('',views.ihas,name="ihas"),
    
    

]
