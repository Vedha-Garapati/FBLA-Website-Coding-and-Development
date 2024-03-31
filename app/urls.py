from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.main,name = 'index'),
    path('work',views.application, name='work' ),
    path('apply', views.applyHere, name='apply'),
    path('thank',views.index,name='thank'),
    path('ai',views.AI,name="ai")

]