from django.urls import path
from django.contrib.auth import views

from .views import HomeView, ProfileView, ScheduleView, ControlView, RedirectProfile

urlpatterns = [
    path('', HomeView.showPage, name='home'),
    path('profile/', ProfileView.showPage, name='profile'),
    path('schedule/', ScheduleView.showPage, name='schedule'),
    path('schedule/<id>', ScheduleView.deletePage, name='remove-schedule'),
    path('schedule/new/', ScheduleView.postPage, name='add-schedule'),
    path('control/', ControlView.showPage, name='control'),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/profile/', RedirectProfile.showPage)
]
