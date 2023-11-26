from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
                                                authentication_form=LoginForm), name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('activate/<str:uidb64>/<str:token>/', views.ActivateAccountView.as_view(), name='activate')
]
