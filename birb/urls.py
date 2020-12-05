from django.contrib import admin
from django.urls import path
from main.views import main_view, delete_view, accounts_view,\
    login_view, signup_view, logout_view, profile_view,\
    delete_view_from_profile, splash_view, user_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('splash/', splash_view, name='splash_view'),
    path('delete/', delete_view, name='delete_view'),
    path('delete_from_profile', delete_view_from_profile, name='delete_view_from_profile'),
    path('accounts/', accounts_view, name='accounts_view'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('profile/', profile_view, name='profile_view'),
    path('user/<str:username>/', user_view, name='user_view'),
]
