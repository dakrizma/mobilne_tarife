from django.forms import ModelForm
from tarife.models import Racun
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class RacunForm(ModelForm):
    class Meta:
        model = Racun
        exclude = ('korisnik',)

# class UserForm(ModelForm):
# 	class Meta:
# 		model = User
# 		get_success_url = lambda: reverse('create_user')
# 		form_class = UserCreationForm
# 		template_name = "register.html"
# 		exclude = ('last_login', 'is_superuser', 'user_permissions', 'groups',  'is_staff', 'is_active', 'date_joined', )

class UserCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and ", "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and ", "@/./+/-/_ characters.")
            }
	)
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user