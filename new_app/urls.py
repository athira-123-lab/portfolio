from django.urls import path
from . import views

urlpatterns = [
    path("",views.createProfile),
    path('listprofile/',views.listProfile),
    path('index',views.index)


]