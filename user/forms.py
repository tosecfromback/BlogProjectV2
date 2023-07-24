from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'nickname', 'password1', 'password2' ]


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = [  'nickname', 'password']


class UserChangeForm(UserChangeForm):
    
    class Meta:
        modle = User
        fields = [ 'nickname' ]


class PasswordUpdateFrom(PasswordChangeForm):

    class Meta:
        model = User
        fields=  [ 'old_password', 'new_password1', 'new_password2']