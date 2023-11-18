import core.mixins
import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms


class CustomAuthForm(
    core.mixins.FormMixin, django.contrib.auth.forms.AuthenticationForm
):
    pass


class CustomPassChangeForm(
    core.mixins.FormMixin, django.contrib.auth.forms.PasswordChangeForm
):
    pass


class CustomPassResetForm(
    core.mixins.FormMixin, django.contrib.auth.forms.PasswordResetForm
):
    pass


class CustomPassResetConfirmForm(
    core.mixins.FormMixin, django.contrib.auth.forms.SetPasswordForm
):
    pass


class SignUpForm(
    core.mixins.FormMixin, django.contrib.auth.forms.UserCreationForm
):
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
