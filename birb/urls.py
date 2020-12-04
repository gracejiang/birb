from django.contrib import admin
from django.urls import path
from main.views import main_view, delete_view, accounts_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('delete/', delete_view, name='delete_view'),
    path('accounts/', accounts_view, name='accounts_view')
]
