from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin

from .models import *
from .forms import *
"""
Этот код импортирует необходимые модули, классы, модели и формы из различных файлов. Классы используются для отображения различных страниц веб-сайта, включая домашнюю страницу, страницу профиля, страницу расписания и страницы управления. Некоторые страницы, в том числе профиль, расписание и страницы управления, требуют, чтобы пользователь вошел в систему. Страницы управления, которые позволяют администраторам управлять пользователями веб-сайта, сообщениями, курсами и т. д., доступны только пользователям с соответствующими правами администратора. привилегии. Код также включает класс для регистрации пользователя (SignupView) и класс для перенаправления пользователя на страницу его профиля (RedirectProfile).
"""


class HomeView(View):

    def showPage(request):
        if request.method == 'GET':
            return render(request, 'index.html')


@login_required()
class ProfileView(View):

    def showPage(request):

        if request.user.is_authenticated:
            user = request.user

            if request.user.is_cursant:
                training = Training.objects.get(id_cursant=user.id)

                return render(request, 'cursant/profile.html', {'user': user, 'training': training})

            elif request.user.is_worker:
                if request.user.id_post == 'Инструктор':
                    return render(request, 'worker/profile.html', {'user': user})

                else:
                    return render(request, 'worker/profile-2.html', {'user': user})

        else:
            return redirect('login')


@login_required()
class ScheduleView(View):

    def showPage(request):

        form = CursantPostScheduleForm(request.POST)

        if request.user is not None and request.user.is_cursant:
            user = request.user
            schedule = Schedule.objects.filter(id_cursant=user.id)

            return render(request, 'cursant/schedule.html', {'schedule': schedule, 'form': form})

        elif request.user is not None and request.user.is_worker:
            user = request.user
            schedule = Schedule.objects.filter(id_worker=user.id)

            return render(request, 'worker/schedule.html', {'schedule': schedule})

        else:
            return redirect('login')

    def deletePage(request, id):
        remove = Schedule.objects.filter(
            id_cursant=request.user.id).filter(id=id).delete()

        return redirect('schedule')

    def postPage(request):
        date = request.POST['date_class']
        time = request.POST['time_class']

        if Schedule.objects.filter(date_class=date) and Schedule.objects.filter(time_class=time):
            message = 'На данное время инструктор занят! Выберите другой день или время.'
            return render(request, 'cursant/schedule.html', {'message': message})

        else:
            schedule_new = Schedule(id_worker=User.objects.get(id=request.POST['id_worker']),
                                    id_discipline=Discipline.objects.get(
                                        id=request.POST['id_discipline']),
                                    id_cursant=request.user,
                                    date_class=date,
                                    time_class=time)

            schedule_new.save()

        return redirect('schedule')


@login_required()
class ControlView(View, FormMixin):

    def showPage(request):

        return redirect('/control/users/')

    # Пользователи
    def usersControlPage(request):
        users = User.objects.all()
        form = WorkerPostUserForm(request.POST)

        return render(request, 'worker/control-users.html', {'users': users, 'form': form})

    # Отфильтрованные пользователи
    def usersFilteredControlPage(request):
        users = User.objects.filter(last_name__regex=r'[А-Я]')

        return render(request, 'worker/control-users.html', {'users': users})

    # Добавление пользователя
    def usersControlPostPage(request):
        form = WorkerPostUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/control/users/')

    # Удаление пользователя
    def usersControlDeletePage(request, id):
        remove = User.objects.filter(id=id).delete()

        return redirect('/control/users/')

    # Редактирование пользователя
    def usersControlUpdatePage(request, id):
        user = User.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerUpdateUserForm(instance=user)
            return render(request, 'worker/forms/update-user.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerUpdateUserForm(request.POST, instance=user)

            if form.is_valid():
                form.save()
                return redirect('/control/users/')

            else:
                return render(request, 'worker/forms/update-user.html', {'form': form})

    # Должности
    def postsControlPage(request):
        posts = Post.objects.all()
        form = WorkerPostPostForm(request.POST)

        return render(request, 'worker/control-posts.html', {'posts': posts, 'form': form})

    # Добавление должностни
    def postsControlPostPage(request):
        post_new = WorkerPostPostForm(request.POST)
        post_new.save()

        return redirect('/control/posts/')

    # Удаление должности
    def postsControlDeletePage(request, id):
        remove = Post.objects.filter(id=id).delete()

        return redirect('/control/posts/')

    # Обновление должности
    def postsControlUpdatePage(request, id):
        post = Post.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostPostForm(instance=post)
            return render(request, 'worker/forms/update-post.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostPostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
                return redirect('/control/posts/')
    # Обучения

    def trainingsControlPage(request):
        trainings = Training.objects.all()
        form = WorkerPostTrainingForm(request.POST)

        return render(request, 'worker/control-trainings.html', {'trainings': trainings, 'form': form})

    # Добавление обучения
    def trainingsControlPostPage(request):
        training_new = WorkerPostTrainingForm(request.POST)
        training_new.save()

        return redirect('/control/trainings/')

    # Удаление обучения
    def trainingsControlDeletePage(request, id):
        remove = Training.objects.filter(id=id).delete()

        return redirect('/control/trainings/')

    # Обновление обучения
    def trainingsControlUpdatePage(request, id):
        training = Training.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostTrainingForm(instance=training)
            return render(request, 'worker/forms/update-training.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostTrainingForm(request.POST, instance=training)

            if form.is_valid():
                form.save()
                return redirect('/control/trainings/')

    # Вождения
    def drivingsControlPage(request):
        drivings = Driving.objects.all()
        form = WorkerPostDrivingForm(request.POST)

        return render(request, 'worker/control-driving.html', {'drivings': drivings, 'form': form})

    # Добавление вождения
    def drivingsControlPostPage(request):
        driving_new = WorkerPostDrivingForm(request.POST)
        driving_new.save()

        return redirect('/control/drivings/')

    # Удаление вождения
    def drivingsControlDeletePage(request, id):
        remove = Driving.objects.filter(id=id).delete()

        return redirect('/control/drivings/')

    # Обновление вождения
    def drivingsControlUpdatePage(request, id):
        driving = Driving.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostDrivingForm(instance=driving)
            return render(request, 'worker/forms/update-driving.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostDrivingForm(request.POST, instance=driving)

            if form.is_valid():
                form.save()
                return redirect('/control/drivings/')

    # Курсы
    def coursesControlPage(request):
        courses = Course.objects.all()
        form = WorkerPostCourseForm(request.POST)

        return render(request, 'worker/control-courses.html', {'courses': courses, 'form': form})

    # Добавление курса
    def coursesControlPostPage(request):
        course_new = WorkerPostCourseForm(request.POST)
        course_new.save()

        return redirect('/control/courses/')

    # Удаление курса
    def coursesControlDeletePage(request, id):
        remove = Course.objects.filter(id=id).delete()

        return redirect('/control/courses/')

    # Обновление курса
    def coursesControlUpdatePage(request, id):
        course = Course.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostCourseForm(instance=course)
            return render(request, 'worker/forms/update-driving.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostCourseForm(request.POST, instance=course)

            if form.is_valid():
                form.save()
                return redirect('/control/courses/')

    # Дисциплины
    def discliplinesControlPage(request):
        disciplines = Discipline.objects.all()
        form = WorkerPostDisciplineForm(request.POST)

        return render(request, 'worker/control-disciplines.html', {'disciplines': disciplines, 'form': form})

    # Добавление дисциплины
    def discliplinesControlPostPage(request):
        discipline_new = WorkerPostDisciplineForm(request.POST)
        discipline_new.save()

        return redirect('/control/disciplines/')

    # Удаление дисциплины
    def discliplinesControlDeletePage(request, id):
        remove = Discipline.objects.filter(id=id).delete()

        return redirect('/control/disciplines/')

    # Обновление дисциплины
    def discliplinesControlUpdatePage(request, id):
        disclipline = Discipline.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostCourseForm(instance=disclipline)
            return render(request, 'worker/forms/update-disclipline.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostCourseForm(request.POST, instance=disclipline)

            if form.is_valid():
                form.save()
                return redirect('/control/discliplines/')

    # Категории
    def categoriesControlPage(request):
        categories = Category.objects.all()
        form = WorkerPostCategoryForm(request.POST)

        return render(request, 'worker/control-categories.html', {'categories': categories, 'form': form})

    # Добавление категории
    def categoriesControlPostPage(request):
        category_new = WorkerPostCategoryForm(request.POST)
        category_new.save()

        return redirect('/control/categories/')

    # Удаление категории
    def categoriesControlDeletePage(request, id):
        remove = Category.objects.filter(id=id).delete()

        return redirect('/control/categories/')
    
    # Обновление категории
    def categoriesControlUpdatePage(request, id):
        category = Category.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostCategoryForm(instance=category)
            return render(request, 'worker/forms/update-category.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostCategoryForm(request.POST, instance=category)

            if form.is_valid():
                form.save()
                return redirect('/control/categories/')

    # Автомобили
    def autosControlPage(request):
        autos = Car.objects.all()
        form = WorkerPostCarForm(request.POST)

        return render(request, 'worker/control-autos.html', {'autos': autos, 'form': form})

    # Добавление автомобиля
    def autosControlPostPage(request):
        car_new = WorkerPostCarForm(request.POST)
        car_new.save()

        return redirect('/control/cars/')

    # Удаление автомобиля
    def autosControlDeletePage(request, id):
        remove = Car.objects.filter(id=id).delete()

        return redirect('/control/cars/')
    
    # Обновление автомобиля
    def autosControlUpdatePage(request, id):
        auto = Car.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostCarForm(instance=auto)
            return render(request, 'worker/forms/update-car.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostCarForm(request.POST, instance=auto)

            if form.is_valid():
                form.save()
                return redirect('/control/cars/')
    
    # Регионы
    def regionsControlPage(request):
        regions = Region.objects.all()
        form = WorkerPostRegionForm(request.POST)

        return render(request, 'worker/control-regions.html', {'regions': regions, 'form': form})

    # Добавление региона
    def regionsControlPostPage(request):
        region_new = WorkerPostRegionForm(request.POST)
        region_new.save()

        return redirect('/control/regions/')

    # Удаление региона
    def regionsControlDeletePage(request, id):
        remove = Region.objects.filter(id=id).delete()

        return redirect('/control/regions/')
    
    # Обновление региона
    def regionsControlUpdatePage(request, id):
        region = Region.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostRegionForm(instance=region)
            return render(request, 'worker/forms/update-region.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostRegionForm(request.POST, instance=region)

            if form.is_valid():
                form.save()
                return redirect('/control/regions/')

    # Города
    def citiesControlPage(request):
        cities = City.objects.all()
        form = WorkerPostCityForm(request.POST)

        return render(request, 'worker/control-cities.html', {'cities': cities, 'form': form})

    # Добавление города
    def citiesControlPostPage(request):
        city_new = WorkerPostCityForm(request.POST)
        city_new.save()

        return redirect('/control/cities/')

    # Удаление города
    def citiesControlDeletePage(request, id):
        remove = City.objects.filter(id=id).delete()

        return redirect('/control/cities/')

    # Обновление города
    def citiesControlUpdatePage(request, id):
        city = City.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostCityForm(instance=city)
            return render(request, 'worker/forms/update-city.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostCityForm(request.POST, instance=regicityon)

            if form.is_valid():
                form.save()
                return redirect('/control/cities/')

    # Улицы
    def streetsControlPage(request):
        streets = Street.objects.all()
        form = WorkerPostStreetForm(request.POST)

        return render(request, 'worker/control-streets.html', {'streets': streets, 'form': form})

    # Добавление улицы
    def streetsControlPostPage(request):
        city_new = WorkerPostStreetForm(request.POST)
        city_new.save()

        return redirect('/control/streets/')

    # Удаление улицы
    def streetsControlDeletePage(request, id):
        remove = Street.objects.filter(id=id).delete()

        return redirect('/control/streets/')
    
    # Обновление улицы
    def streetsControlUpdatePage(request, id):
        street = Street.objects.get(id=id)
        if request.method == 'GET':
            form = WorkerPostStreetForm(instance=street)
            return render(request, 'worker/forms/update-street.html', {'form': form})

        elif request.method == 'POST':
            form = WorkerPostStreetForm(request.POST, instance=street)

            if form.is_valid():
                form.save()
                return redirect('/control/streets/')


class RedirectProfile(View):

    def showPage(request):
        return redirect('/profile/')


class SignupView(View):

    def showPage(request):
        message = ""

        if request.user.is_authenticated:
            return redirect("/profile/")
        else:
            if request.method == "GET":
                form = SignupForm()

            if request.method == "POST":
                form = SignupForm(request.POST)

                print(request.POST)

                if form.is_valid():
                    user = form
                    user.save()
                    message = "Успешная регистрация!"
                    return redirect('/profile/')
                else:
                    message = "Введите корректные данные"
                    form = SignupForm()

            return render(request, "registration/signup.html", {"form": form, "message": message})
