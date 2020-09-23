from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import EonsUser


class EonsUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = EonsUser
        fields = ('email',)


class EonsUserChangeForm(UserChangeForm):
    class Meta:
        model = EonsUser
        fields = ('email',)