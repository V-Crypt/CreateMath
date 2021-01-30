from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import GRUPO_POR_GRADO, Actividad
from .forms import *
# Create your views here.
def home(request):
    template_name="home/home.html"
    if request.user.is_authenticated:
        actividades = list()
        for group in request.user.groups.all():
            actividades.append(
                list(group.actividad_set.all())
            )
        
        return render(request, template_name, context={
            "actividades": actividades
        })
    else:
        group = Group.objects.get(name="PUBLIC")
        actividades = [group.actividad_set.all()]
        return render(request, "home/home.html", context={
            "actividades": [Actividad.objects.all()]
        })


def log_user_out(request):
    logout(request)
    return redirect("home:home")

def sign_up(request):

    if request.user.is_authenticated:
        return redirect("home:home")
    
    form = UserCreationForm_custom(request.POST or None)
    studentForm = StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid() and studentForm.is_valid():
            user = form.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            grupo, b = Group.objects.get(name=GRUPO_POR_GRADO[student.grado])
            grupo.user_set.add(user)
            login(request,user)
            return redirect('home:home')
    
    context = {"form": form, "studentForm": studentForm}
    return render(request,'registration/sign_up.html',context)