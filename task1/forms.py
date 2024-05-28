from django import forms
from . models import RegisterUser, TaskAssign
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    username = forms.CharField(required=True, label='Name')
    mobile_number = forms.IntegerField(required=True, label='Mobile Number')
    address = forms.CharField(widget=forms.Textarea, required=True, label='Address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        
        if commit:
            user.save()
            RegisterUser.objects.create(
                user=user,
                mobile_number=self.cleaned_data['mobile_number'],
                address=self.cleaned_data['address']
            )
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput())


class TaskAssignForm(forms.ModelForm):
    class Meta:
        model=TaskAssign
        fields='__all__'
        exclude=['assigned_by']
        widgets={
            'date':forms.DateInput( attrs={'type':'date'}),
            'time':forms.TimeInput( attrs={'type':'time'}),
        }

    