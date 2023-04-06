from django.urls import path
from django.contrib.auth import views

from .views import HomeView, SignupView, ProfileView, ScheduleView, ControlView, RedirectProfile
"""
Этот код содержит список URL-адресов приложения, использующих фреймворк Django. Он описывает маршруты и вызываемые вьюхи, связанные с каждым маршрутом. Маршруты включают маршруты для показа и удаления страниц, создания новых страниц, а также маршруты для управления пользователями, сообщениями, курсами, машинами и т.д. Также включены стандартные маршруты для страницы входа и страницы регистрации пользователя.
"""

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
    path('control/disciplines/new/', ControlView.discliplinesControlPostPage, name='add-discipline'),
    path('control/disciplines/<id>', ControlView.discliplinesControlDeletePage, name='remove-discipline'),
    path('control/categories/', ControlView.categoriesControlPage, name='control-categories'),
    path('control/categories/new/', ControlView.discliplinesControlPostPage, name='add-category'),
    path('control/categories/<id>', ControlView.discliplinesControlDeletePage, name='remove-category'),
    path('control/cars/', ControlView.autosControlPage, name='control-autos'),
    path('control/cars/new/', ControlView.autosControlPostPage, name='add-car'),
    path('control/cars/<id>', ControlView.autosControlDeletePage, name='remove-car'),
    path('control/regions/', ControlView.regionsControlPage, name='control-regions'),
    path('control/regions/new/', ControlView.regionsControlPostPage, name='add-region'),
    path('control/regions/<id>', ControlView.regionsControlDeletePage, name='remove-region'),
    path('control/cities/', ControlView.citiesControlPage, name='control-cities'),
    path('control/cities/new/', ControlView.citiesControlPostPage, name='add-city'),
    path('control/cities/<id>', ControlView.citiesControlDeletePage, name='remove-city'),
    path('control/streets/', ControlView.streetsControlPage, name='control-streets'),
    path('control/streets/new/', ControlView.streetsControlPostPage, name='add-street'),
    path('control/streets/<id>', ControlView.streetsControlDeletePage, name='remove-street'),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignupView.showPage, name='signup'),
    path('accounts/profile/', RedirectProfile.showPage)
]