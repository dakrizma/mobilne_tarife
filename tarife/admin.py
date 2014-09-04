from django.contrib import admin
from tarife.models import Mreza, Tarifa

class MrezaAdmin(admin.ModelAdmin):
	list_display = ('id', 'ime_mreze')

class TarifaAdmin(admin.ModelAdmin):
	list_display = ('id', 'ime_tarife', 'prim_cij', 'druge_cij', 'sms_cij', 'mms_cij', 'net_cij', 'prim', 'druge', 'sms', 'mms', 'net', 'uspostava', 'naknada', 'pretplata','mreza')
	list_filter = ('mreza',)

admin.site.register(Mreza, MrezaAdmin)
admin.site.register(Tarifa, TarifaAdmin)