from rest_framework import serializers
from django.contrib.auth.models import User
from .models import RegisterUser, DepratmentUser, TaskAssign

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterUser
        fields='__all__'

class DepartmentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepratmentUser
        fields='__all__'

class TaskAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAssign
        fields='__all__'