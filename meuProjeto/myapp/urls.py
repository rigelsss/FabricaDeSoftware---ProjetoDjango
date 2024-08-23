from django.urls import path
from . import views

urlpatterns = [
    # URLs para Autor
    path('autor/', views.autor_list, name='autor_list'),
    path('autor/<int:pk>/', views.autor_detail, name='autor_detail'),
    path('autor/new/', views.autor_create, name='autor_create'),
    path('autor/<int:pk>/edit/', views.autor_update, name='autor_update'),
    path('autor/<int:pk>/delete/', views.autor_delete, name='autor_delete'),

    # URLs para Book
    path('artigo/', views.artigo_list, name='artigo_list'),
    path('artigo/<int:pk>/', views.artigo_detail, name='artigo_detail'),
    path('artigo/new/', views.artigo_create, name='artigo_create'),
    path('artigo/<int:pk>/edit/', views.artigo_update, name='artigo_update'),
    path('artigo/<int:pk>/delete/', views.artigo_delete, name='artigo_delete'),
]