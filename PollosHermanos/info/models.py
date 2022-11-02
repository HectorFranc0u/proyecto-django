# Rene Fuentes
# Hector Franco
# David Hernandez
# Geovanny Mauricio

from operator import mod
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class tbProductos(models.Model):
    ProdName = models.CharField(max_length=200)
    ProdTipo = models.CharField(max_length=200)
    ProdUnidaddeMed = models.CharField(max_length=10)
    ProdName = models.CharField(max_length=5)
    idProveedor = models.CharField(max_length=10)

class tbCombos(models.Model):
    CombName = models.CharField(max_length=200)
    CombTipo = models.CharField(max_length=200)
    ComPrecio = models.CharField(max_length=10)
    CombDescripcion = models.CharField(max_length=200)
    CombDisp = models.BooleanField()
    idProducto = models.CharField(max_length=10)

class tbSucursales(models.Model):
    SucName = models.CharField(max_length=200)
    SucAddress = models.TextField()
    SucGerente = models.CharField(max_length=200)
    SucHorarios = models.CharField(max_length=200)
    SucCombos = models.CharField(max_length=200)
    idCombos = models.CharField(max_length=10)

class tbProveedores(models.Model):
    ProvEmpresa = models.CharField(max_length=200)
    ProvName = models.CharField(max_length=200)
    ProvLastname = models.CharField(max_length=200)
    ProvPais = models.CharField(max_length=200)
    ProvTipoProd = models.CharField(max_length=200)
    idSucursal = models.CharField(max_length=200)