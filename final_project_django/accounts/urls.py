from django.urls import path, include
from . import views
from accounts.views import UserAPIView

app_name = 'accounts'

urlpatterns = [
    path('', UserAPIView.as_view(), name='user'),
    path('admin/', views.admin_accounts, name='admin_accounts'),
    # path('signup/', views.signup, name='signup'),
    # path('signout/', views.signout, name='signout'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('rest-auth/', include("rest_auth.urls")),
    path('signup/', include("rest_auth.registration.urls")),
]