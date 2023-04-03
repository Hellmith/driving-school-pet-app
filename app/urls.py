from django.urls import path
from django.contrib.auth import views

from .views import HomeView, SignupView, ProfileView, ScheduleView, ControlView, RedirectProfile

urlpatterns = [
    path('', HomeView.showPage, name='home'),
    path('profile/', ProfileView.showPage, name='profile'),
    path('schedule/', ScheduleView.showPage, name='schedule'),
    path('schedule/<id>', ScheduleView.deletePage, name='remove-schedule'),
    path('schedule/new/', ScheduleView.postPage, name='add-schedule'),
    path('control/', ControlView.showPage, name='control'),
    path('control/users/', ControlView.usersControlPage, name='control-users'),
    path('control/disciplines/', ControlView.discliplinesControlPage, name='control-disciplines'),
    path('control/cars/', ControlView.autosControlPage, name='control-autos'),
    path('control/regions/', ControlView.regionsControlPage, name='control-regions'),
    path('control/cities/', ControlView.citiesControlPage, name='control-cities'),
    path('control/streets/', ControlView.streetsControlPage, name='control-streets'),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignupView.showPage, name='signup'),
    path('accounts/profile/', RedirectProfile.showPage)
]