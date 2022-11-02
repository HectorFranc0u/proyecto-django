from django.contrib import admin
from .models import tbCombos, tbProductos, tbProveedores, tbSucursales

# Register your models here.
admin.site.register(tbCombos)
admin.site.register(tbSucursales)
admin.site.register(tbProveedores)
admin.site.register(tbProductos)