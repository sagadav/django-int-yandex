import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms


class CustomAuthForm(django.contrib.auth.forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class CustomPassChangeForm(django.contrib.auth.forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class CustomPassResetForm(django.contrib.auth.forms.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class CustomPassResetConfirmForm(django.contrib.auth.forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = django.contrib.auth.models.User
        fields = ["email", "username", "password1", "password2"]


class ProfileForm(django.forms.ModelForm):
    birthday = django.forms.DateField()
    image = django.forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs["instance"]
        if instance:
            if instance.profile:
                self.fields["birthday"].label = "День рождения"
                self.fields["birthday"].initial = instance.profile.birthday
                self.fields["image"].label = "Картинка"
                self.fields["image"].initial = instance.profile.image
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = django.contrib.auth.models.User
        fields = ["email", "first_name", "birthday", "image"]
