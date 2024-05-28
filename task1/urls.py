from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register(r'register', views.RegisterUserViewSet, basename='register')
routers.register(r'department-user',views.DepartmentUserViewSet, basename='department-user')
routers.register(r'task-assign', views.TaskAssignViewSet, basename='task-assign')
urlpatterns = [
    path('api/',include(routers.urls)),
    path('register',views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('assign_task/<str:name>/', views.task_assign_view, name='assign-task'),
]