from django.forms import ModelForm
from tarife.models import Racun
from django.utils.translation import ugettext_lazy as _

class RacunForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'prim': _('Pozivi prema primarnoj mrezi'),
			'druge': _('Pozivi prema drugim mrezama'),
			'sms': _('Broj poslanih sms-ova'),
			'mms': _('Broj poslanih mms-ova'),
			'net': _('Kolicina potrosenog prometa u MB'),
			'mjesec': _('Mjesec racuna'),
			'godina': _('Godina racuna'),
			}
        exclude = ('korisnik',)