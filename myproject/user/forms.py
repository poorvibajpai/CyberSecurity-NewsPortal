from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('textbox', 'number', 'email','textbox')