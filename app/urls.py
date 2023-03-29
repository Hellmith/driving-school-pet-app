from django.urls import path
from django.contrib.auth import views

from .views import HomeView, AboutView, ProfileView, RegisterCadetView, RegisterInstructorView, RegisterOperView

urlpatterns = [
    path('', HomeView.get, name='home'),
    path('about/', AboutView.get, name='about'),
    path('profile/', ProfileView.get, name='profile'),
    path(
        'login/',
        views.LoginView.as_view(redirect_authenticated_user=True),
        name='login',
    ),
    path('reg-cadet/', RegisterCadetView.get, name='reg-cadet'),
    path('reg-intructor/', RegisterInstructorView.get, name='reg-instructor'),
    path('reg-oper/', RegisterOperView.get, name='reg-oper'),
]
