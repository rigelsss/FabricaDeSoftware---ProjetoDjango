from django.contrib import admin

# Register your models here.
from .models import Autor

# Registre o modelo Author para aparecer na interface de administração
admin.site.register(Autor)