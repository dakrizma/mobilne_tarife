from django.forms import ModelForm
from tarife.models import Racun
from django.contrib.auth.models import User

class RacunForm(ModelForm):
    class Meta:
        model = Racun

class UserForm(ModelForm):
	class Meta:
		model = User