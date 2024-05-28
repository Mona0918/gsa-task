from django.shortcuts import render
from .models import RegisterUser, TaskAssign, DepratmentUser
from .forms import RegisterUserForm, LoginForm, TaskAssignForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterUserSerializer, DepartmentUserSerializer, TaskAssignSerializer

class RegisterUserViewSet(ModelViewSet):
    queryset=RegisterUser.objects.all()
    serializer_class=RegisterUserSerializer

class DepartmentUserViewSet(ModelViewSet):
    queryset=DepratmentUser.objects.all()
    serializer_class=DepartmentUserSerializer

class TaskAssignViewSet(ModelViewSet):
    queryset=TaskAssign.objects.all()
    serializer_class=TaskAssignSerializer


def register_view(request):
    if request.method=='POST':
        register_form = RegisterUserForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('login'))
    else:
        register_form = RegisterUserForm()
    return render(request, 'register.html',{'register_form':register_form})

def login_view(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                print(user)
            except User.DoesNotExist:
                user = None
            password = form.cleaned_data['password']
            print(password, user)
            if user:
                a_user=authenticate(request,username=user.username,password=password)
                if a_user is not None:
                    login(request,a_user)
                    return redirect(reverse('dashboard'))
                else:
                    return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

@login_required
def dashboard_view(request):
    tasks=TaskAssign.objects.filter(assigned_by=request.user.username)
    return render(request,'dashboard1.html',{'tasks':tasks})

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@login_required
def task_assign_view(request, name):
    if request.method=='POST':
        form=TaskAssignForm(data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            user = RegisterUser.objects.get(user__username=name)
            instance.assigned_by=user.user.username
            instance.save()
            return redirect(reverse('dashboard'))
    else:
        form = TaskAssignForm()
    return render(request, 'assign_task.html',{'form':form})
    