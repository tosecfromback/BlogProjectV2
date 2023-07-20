from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'email', 'nickname', 'password1', 'password2' ]


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = [ 'email', 'password']


class UserChangeForm(UserChangeForm):
    
    class Meta:
        modle = User
        fields = [ 'email', 'nickname' ]


class PasswordUpdateFrom(PasswordChangeForm):

    class Meta:
        model = User
        fields=  [ 'old_password', 'new_password1', 'new_password2']