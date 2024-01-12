from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('work',views.application, name='work' ),
    path('apply', views.applyHere, name='apply')
]