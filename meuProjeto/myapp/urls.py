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
    path('detalhe/', views.detalhe_list, name='detalhe_list'),
    path('detalhe/<int:pk>/', views.detalhe_detail, name='detalhe_detail'),
    path('detalhe/new/', views.detalhe_create, name='detalhe_create'),
    path('detalhe/<int:pk>/edit/', views.detalhe_update, name='detalhe_update'),
    path('detalhe/<int:pk>/delete/', views.detalhe_delete, name='detalhe_delete'),


    # Nova rota para buscar autores da API externa
    path('fetch-autors/', views.fetch_autors_from_api, name='fetch_autors'),

]