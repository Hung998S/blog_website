from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1','password2')