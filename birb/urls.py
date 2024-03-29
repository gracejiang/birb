from django.contrib import admin
from django.urls import path
import main.views as views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('splash/', views.splash_view, name='splash_view'),
    path('delete/', views.delete_view, name='delete_view'),
    path('accounts/', views.accounts_view, name='accounts_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('user/<str:username>/', views.user_view, name='user_view'),
    path('tag/<str:tag>/', views.hashtag_view, name='hashtag_view'),
    path('like/', views.like_chirp, name='like_chirp'),
]
