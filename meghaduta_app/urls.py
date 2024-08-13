from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('',views.index,name='index'),
    path('sandhi/',views.sandhi,name='sandhi'),
    path('slokas/',views.slokas,name='slokas'),
    path('samasam/',views.samasam,name='samasam'),
    path('slokaselected/<str:uid>',views.slokaselected,name='slokaselected'),
]
