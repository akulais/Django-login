# from django import forms
# from django.forms import ModelForm
# from .models import User

# class User_form(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = "__all__"

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_form(UserCreationForm):
    username = forms.CharField(label='User name', max_length=200)
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    # email = forms.EmailField(label='Email', widget=forms.Textarea, max_length=200)
    # password = forms.CharField(label='Pwd', widget=forms.PasswordInput)
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(User_form, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # user.password = self.cleaned_data['password1']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user

class Auth_form(forms.Form):
    username = forms.CharField(label='User name', widget=forms.TextInput)
    password = forms.CharField(label='Pwd', widget=forms.PasswordInput)
    class Meta:
        fields = ('username', 'password')