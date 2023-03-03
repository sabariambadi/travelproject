from . import views
from django.urls import path


urlpatterns = [

    path('',views.home,name='demo'),
    # path('',views.insta,name='insta'),
]