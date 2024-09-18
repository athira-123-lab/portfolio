from django.urls import path
from . import views


urlpatterns = [
    path("",views.createProfile),

    path('index',views.index),

    path('listprofile/',views.listProfile,name='listprofile'),
]
