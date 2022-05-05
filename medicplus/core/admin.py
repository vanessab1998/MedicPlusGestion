from django.contrib import admin
from .models import hora, pais, region, gender, comuna, paciente, usercontact, pago, areaMedica, doctor, \
comprobante, horaMedica, informe, secretaria, tipoPago, hora

class userscontact(admin.ModelAdmin):
    list_display = ["nameContact", "email", "msn", "created_date"]
    search_fields = ["nom"]



# Register your models here.

admin.site.register(usercontact, userscontact)
admin.site.register(paciente)
admin.site.register(comuna)
admin.site.register(gender)
admin.site.register(pais)
admin.site.register(region)
admin.site.register(horaMedica)
admin.site.register(informe)
admin.site.register(secretaria)
admin.site.register(tipoPago)
admin.site.register(pago)
admin.site.register(areaMedica)
admin.site.register(doctor)
admin.site.register(comprobante)
admin.site.register(hora)
