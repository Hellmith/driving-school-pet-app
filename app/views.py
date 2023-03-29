from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import *


class HomeView(View):

    def get(request):
        return render(request, 'index.html')


class AboutView(View):

    def get(request):
        return render(request, 'about.html')


@login_required()
class ProfileView(View):

    def get(request):
        return render(request, 'profile.html')


class RegisterCadetView(View):

    def get(request):
        message = ''

        if request.user.is_authenticated:
            return redirect('home')

        else:
            if request.method == 'GET':
                form = RegisterCadetForm()

            if request.method == 'POST':
                form = RegisterCadetForm(request.POST)

                if form.is_valid():
                    user = form
                    user.save()

                    return redirect('login')

                else:
                    message = 'Данные введены некорректно.'
                    form = RegisterCadetForm()

            return render(request, 'registration/register-cadet.html', {'form': form, 'message': message})


class RegisterInstructorView(View):

    def get(request):
        message = ''

        if request.user.is_authenticated:
            return redirect('home')

        else:
            if request.method == 'GET':
                form = RegisterInstructorForm()

            if request.method == 'POST':
                form = RegisterInstructorForm(request.POST)

                if form.is_valid():
                    user = form
                    user.save()

                    return redirect('login')

                else:
                    message = 'Данные введены некорректно.'
                    form = RegisterInstructorForm()

            return render(request, 'registration/register-instructor.html', {'form': form, 'message': message})


class RegisterOperView(View):

    def get(request):
        message = ''

        if request.user.is_authenticated:
            return redirect('home')

        else:
            if request.method == 'GET':
                form = RegisterOperForm()

            if request.method == 'POST':
                form = RegisterOperForm(request.POST)

                if form.is_valid():
                    user = form
                    user.save()

                    return redirect('login')

                else:
                    message = 'Данные введены некорректно.'
                    form = RegisterOperForm()

            return render(request, 'registration/register-oper.html', {'form': form, 'message': message})
