from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.admin_accounts, name='admin_accounts'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]