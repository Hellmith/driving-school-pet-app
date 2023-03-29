from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import Training
from .forms import *


class HomeView(View):

    def get(request):
        return render(request, 'index.html')


@login_required()
class ProfileView(View):

    def get(request):

        if request.user is not None and request.user.is_cursant:
            user = request.user

            training = Training.objects.get(id_cursant=user.id)

            return render(request, 'cursant/profile.html', {'user': user, 'training': training})