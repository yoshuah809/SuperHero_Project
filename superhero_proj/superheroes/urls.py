from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('new/', views.create, name= 'create'),
    path('save/', views.process_form, name= 'savehero'),

    path ('show/<int:id>/', views.show, name= 'show'),
    path ('edit/<int:id>/', views.edit, name= 'edit'),
    path ('update/<int:id>/', views.update, name= 'update'),
    path ('form/', views.form, name= 'form'),
    path ('display/', views.list_heroes, name= 'display'),
    path ('delete/<int:id>/', views.delete, name= 'delete')

]
