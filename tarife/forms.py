from django.forms import ModelForm
from tarife.models import Racun
from django.utils.translation import ugettext_lazy as _

class RacunForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'prim': _('Pozivi prema primarnoj mreži'),
			'druge': _('Pozivi prema drugim mrežama'),
			'sms': _('Broj poslanih sms-ova'),
			'mms': _('Broj poslanih mms-ova'),
			'net': _('Količina potrošenog prometa u MB'),
			'mjesec': _('Mjesec računa'),
			'godina': _('Godina računa'),
			}
        exclude = ('korisnik',)