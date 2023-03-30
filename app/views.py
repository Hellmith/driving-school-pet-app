from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import Training, Schedule, User
from .forms import CursantPostSchedule


class HomeView(View):

    def showPage(request):
        if request.method == 'GET':
            return render(request, 'index.html')


@login_required()
class ProfileView(View):

    def showPage(request):

        if request.user is not None and request.user.is_cursant:
            user = request.user
            training = Training.objects.get(id_cursant=user.id)

            return render(request, 'cursant/profile.html', {'user': user, 'training': training})

        elif request.user is not None and request.user.is_worker:
            user = request.user
            return render(request, 'worker/profile.html', {'user': user})

        else:
            return redirect('login')


@login_required()
class ScheduleView(View):

    def showPage(request):

        if request.user is not None and request.user.is_cursant:
            user = request.user
            schedule = Schedule.objects.filter(id_cursant=user.id)

            form = CursantPostSchedule(request.POST or None)
            if form.is_valid():
                print("\n\n form is valid")

                schedule = form.save(commit=False)
                schedule.id_worker = request.POST['id_worker']
                schedule.id_discipline = request.POST['id_discipline']
                schedule.id_cursant = request.user
                schedule.date_class = request.POST['date_class']
                schedule.time_class = request.POST['time_class']
                schedule.save()

                return redirect('schedule')

            return render(request, 'cursant/schedule.html', {'schedule': schedule, 'form': form})

        elif request.user is not None and request.user.is_worker:
            user = request.user
            schedule = Schedule.objects.filter(id_worker=user.id)

            return render(request, 'worker/schedule.html', {'schedule': schedule})

        else:
            return redirect('login')

    def actionPage(request, id):
        remove = Schedule.objects.filter(id_cursant=request.user.id).filter(id=id).delete()

        return redirect('schedule')
