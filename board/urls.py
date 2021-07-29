from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.upload, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('total-rank/', views.total_rank, name="total-rank"),
    path('big-rank/', views.big_rank, name="big-rank"),
    path('small-rank/', views.small_rank, name="small-rank"),
    path('gas-rank/', views.gas_rank, name="gas-rank"),
]