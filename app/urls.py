from django.urls import path
from django.contrib.auth import views

from .views import HomeView, ProfileView, ScheduleView

urlpatterns = [
    path('', HomeView.showPage, name='home'),
    path('profile/', ProfileView.showPage, name='profile'),
    path('schedule/', ScheduleView.showPage, name='schedule'),
    path('schedule/<id>', ScheduleView.actionPage, name='remove-schedule'),
    path(
        'login/',
        views.LoginView.as_view(redirect_authenticated_user=True),
        name='login',
    )
]
