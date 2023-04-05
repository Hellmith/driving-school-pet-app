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
    path('control/users/new/', ControlView.usersControlPostPage, name='add-user'),
    path('control/users/<id>', ControlView.usersControlDeletePage, name='remove-user'),
    # path('control/users/<int:pk>', ControlView.usersControlUpdatePage, name='update-user'),
    path('control/posts/', ControlView.postsControlPage, name='control-posts'),
    path('control/posts/new/', ControlView.postsControlPostPage, name='add-post'),
    path('control/posts/<id>', ControlView.postsControlDeletePage, name='remove-post'),
    path('control/trainings/', ControlView.trainingsControlPage, name='control-trainings'),
    path('control/trainings/new/', ControlView.trainingsControlPostPage, name='add-training'),
    path('control/trainings/<id>', ControlView.trainingsControlDeletePage, name='remove-training'),
    path('control/driving/', ControlView.drivingsControlPage, name='control-driving'),
    path('control/driving/new/', ControlView.drivingsControlPostPage, name='add-driving'),
    path('control/driving/<id>', ControlView.drivingsControlDeletePage, name='remove-driving'),
    path('control/courses/', ControlView.coursesControlPage, name='control-courses'),
    path('control/courses/new/', ControlView.coursesControlPostPage, name='add-course'),
    path('control/courses/<id>', ControlView.coursesControlDeletePage, name='remove-course'),
    path('control/disciplines/', ControlView.discliplinesControlPage, name='control-disciplines'),
    path('control/categories/', ControlView.categoriesControlPage, name='control-categories'),
    path('control/cars/', ControlView.autosControlPage, name='control-autos'),
    path('control/regions/', ControlView.regionsControlPage, name='control-regions'),
    path('control/cities/', ControlView.citiesControlPage, name='control-cities'),
    path('control/streets/', ControlView.streetsControlPage, name='control-streets'),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignupView.showPage, name='signup'),
    path('accounts/profile/', RedirectProfile.showPage)
]