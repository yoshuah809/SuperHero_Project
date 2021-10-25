from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('new/', views.create, name= 'create'),
    path ('<int:hero_id>/', views.detail, name= 'detail'),
    path ('update/<int:id>/', views.update, name= 'update')
]
