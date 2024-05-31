from django.urls import path
from . import views


app_name='homeFa'
urlpatterns=[
    path('',views.home_fa,name='home'),
]