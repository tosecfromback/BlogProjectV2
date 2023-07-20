from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegisterFrom(UserCreationForm):

    class Meta:
        model = User
        fields = [  'email', 'nickname','password1', 'password2' ]


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = [ 'email', 'password']


class UserChangeForm(UserChangeForm):
    
    class Meta:
        modle = User
        fields = [ 'nickname', 'email' ]


class PasswordUpdateFrom(PasswordChangeForm):

    class Meta:
        model = User
        fields=  [ 'old_password', 'new_password1', 'new_password2']