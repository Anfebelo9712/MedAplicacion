from django.db import models
from .user import Usuario
from .auxiliar import Auxiliar
from .medico import Medico
    
class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario,related_name = 'id_usuario_paciente',on_delete=models.CASCADE,unique=True)
    fecha_creacion = models.DateField('create_date')
    direccion = models.CharField('residencia',max_length=50)
    ciudad = models.CharField('Ciudad',max_length=20)
    id_registro = models.ForeignKey(Auxiliar,related_name = 'id_registro_paciente',on_delete=models.CASCADE)
    
