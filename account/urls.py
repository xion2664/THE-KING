from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('delete/', views.user_delete, name="delete"),
    path('mypage/', views.mypage, name="mypage"),
    path('update/', views.user_update, name='update'),
    path('rank/', views.rank, name='rank'),
    path('history/', views.history, name='history'),
    path('people/', views.people, name='people'),
]