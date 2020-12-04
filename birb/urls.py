from django.contrib import admin
from django.urls import path
from main.views import main_view, home_view, delete_view, accounts_view,\
    login_view, signup_view, logout_view, profile_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('home/', home_view, name='home_view'),
    path('admin/', admin.site.urls),
    path('delete/', delete_view, name='delete_view'),
    path('accounts/', accounts_view, name='accounts_view'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('profile/', profile_view, name='profile_view')
]
