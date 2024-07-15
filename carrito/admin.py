from django.contrib import admin
from .models import Orden , DireccionEnvio , ProductosComprados
# Register your models here.

admin.site.register(Orden)
admin.site.register(DireccionEnvio)
admin.site.register(ProductosComprados)