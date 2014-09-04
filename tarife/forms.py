from django.forms import ModelForm
from tarife.models import Racun

class RacunForm(ModelForm):
    class Meta:
        model = Racun
