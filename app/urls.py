from django.urls import path
from django.contrib.auth import views

from .views import *
"""
Этот код содержит список URL-адресов приложения, использующих фреймворк Django. Он описывает маршруты и вызываемые вьюхи, связанные с каждым маршрутом. Маршруты включают маршруты для показа и удаления страниц, создания новых страниц, а также маршруты для управления пользователями, сообщениями, курсами, машинами и т.д. Также включены стандартные маршруты для страницы входа и страницы регистрации пользователя.
"""

urlpatterns = [

    # Главная страница
    path('', HomeView.showPage, name='home'),

    # Личный кабинет
    path('profile/', ProfileView.showPage, name='profile'),

    # Расписание
    path('schedule/', ScheduleView.showPage, name='schedule'),
    path('schedule/<id>', ScheduleView.deletePage, name='remove-schedule'),
    path('schedule/new/', ScheduleView.postPage, name='add-schedule'),

    # Управление
    path('control/', ControlView.showPage, name='control'),
    
    # Группы
    path('by-groups/', ControlView.usersByGroupPage, name='by-grops'),
    
    # Рассписания
    path('schedules/', ControlView.usersSchedulesPage, name='schedules'),

    # Курсанты
    path('cursants/', CursantsView.showPage, name='cursants'),
    path('cursants/<id>/', CursantsView.showPage, name='cursants-by-course'),

    # Пользователи
    path('control/users/', ControlView.usersControlPage, name='control-users'),
    path('control/users/filter=last_name', ControlView.usersFilteredControlPage, name='filtered-control-users'),
    path('control/user/new/', ControlView.usersControlPostPage, name='add-user'),
    path('control/user/<id>', ControlView.usersControlDeletePage, name='remove-user'),
    path('control/user/<id>/update', ControlView.usersControlUpdatePage, name='update-user'),

    # Должности
    path('control/posts/', ControlView.postsControlPage, name='control-posts'),
    path('control/post/new/', ControlView.postsControlPostPage, name='add-post'),
    path('control/post/<id>', ControlView.postsControlDeletePage, name='remove-post'),
    path('control/post/<id>/update', ControlView.postsControlUpdatePage, name='update-post'),

    # Обучение
    path('control/trainings/', ControlView.trainingsControlPage, name='control-trainings'),
    path('control/training/new/', ControlView.trainingsControlPostPage, name='add-training'),
    path('control/training/<id>', ControlView.trainingsControlDeletePage, name='remove-training'),
    path('control/training/<id>/update', ControlView.trainingsControlUpdatePage, name='update-training'),

    # Вождения
    path('control/drivings/', ControlView.drivingsControlPage, name='control-drivings'),
    path('control/driving/new/', ControlView.drivingsControlPostPage, name='add-driving'),
    path('control/driving/<id>', ControlView.drivingsControlDeletePage, name='remove-driving'),
    path('control/driving/<id>/update', ControlView.drivingsControlUpdatePage, name='update-driving'),

    # Курсы
    path('control/courses/', ControlView.coursesControlPage, name='control-courses'),
    path('control/course/new/', ControlView.coursesControlPostPage, name='add-course'),
    path('control/course/<id>', ControlView.coursesControlDeletePage, name='remove-course'),
    path('control/course/<id>/update', ControlView.coursesControlUpdatePage, name='update-course'),

    # Дисциплины
    path('control/disciplines/', ControlView.discliplinesControlPage, name='control-disciplines'),
    path('control/discipline/new/', ControlView.discliplinesControlPostPage, name='add-discipline'),
    path('control/discipline/<id>', ControlView.discliplinesControlDeletePage, name='remove-discipline'),
    path('control/discipline/<id>/update', ControlView.discliplinesControlUpdatePage, name='update-discipline'),

    # Категории
    path('control/categories/', ControlView.categoriesControlPage, name='control-categories'),
    path('control/category/new/', ControlView.categoriesControlPostPage, name='add-category'),
    path('control/category/<id>', ControlView.categoriesControlDeletePage, name='remove-category'),
    path('control/category/<id>/update', ControlView.categoriesControlUpdatePage, name='update-category'),

    # Автомобили
    path('control/cars/', ControlView.autosControlPage, name='control-autos'),
    path('control/car/new/', ControlView.autosControlPostPage, name='add-car'),
    path('control/car/<id>', ControlView.autosControlDeletePage, name='remove-car'),
    path('control/car/<id>/update', ControlView.autosControlUpdatePage, name='update-car'),

    # Регионы
    path('control/regions/', ControlView.regionsControlPage, name='control-regions'),
    path('control/region/new/', ControlView.regionsControlPostPage, name='add-region'),
    path('control/region/<id>', ControlView.regionsControlDeletePage, name='remove-region'),
    path('control/region/<id>/update', ControlView.regionsControlUpdatePage, name='update-region'),

    # Города
    path('control/cities/', ControlView.citiesControlPage, name='control-cities'),
    path('control/city/new/', ControlView.citiesControlPostPage, name='add-city'),
    path('control/city/<id>', ControlView.citiesControlDeletePage, name='remove-city'),
    path('control/city/<id>/update', ControlView.citiesControlUpdatePage, name='update-city'),

    # Улицы
    path('control/streets/', ControlView.streetsControlPage, name='control-streets'),
    path('control/street/new/', ControlView.streetsControlPostPage, name='add-street'),
    path('control/street/<id>', ControlView.streetsControlDeletePage, name='remove-street'),
    path('control/street/<id>/update', ControlView.streetsControlUpdatePage, name='update-street'),

    # Авторизация
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignupView.showPage, name='signup'),

    # Прочее
    path('accounts/profile/', RedirectProfile.showPage)
]
