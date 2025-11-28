from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alumno')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curp = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    intento = models.IntegerField(default=1)

    class Meta:
        unique_together = ('alumno', 'curso')

    def __str__(self):
        return f"{self.alumno} inscrito en {self.curso}"

class Actividad(models.Model):
    """
    Modelo para actividades/tareas de un curso.
    """
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='actividades')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=100.00, 
                                help_text="Valor máximo de la actividad (ej: 100 puntos)")
    tipo = models.CharField(max_length=20, choices=[
        ('tarea', 'Tarea'),
        ('examen', 'Examen'),
        ('proyecto', 'Proyecto'),
        ('participacion', 'Participación'),
    ], default='tarea')
    estado = models.CharField(max_length=20, choices=[
        ('activa', 'Activa'),
        ('cerrada', 'Cerrada'),
    ], default='activa')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['-fecha_limite']

    def __str__(self):
        return f"{self.nombre} - {self.curso}"


class CalificacionActividad(models.Model):
    """
    Calificaciones de actividades por alumno.
    """
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='calificaciones')
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name='calificaciones_actividades')
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                       help_text="Calificación obtenida")
    fecha_calificacion = models.DateField(auto_now_add=True)
    comentarios = models.TextField(blank=True, null=True)
    entregado = models.BooleanField(default=False)
    fecha_entrega = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('actividad', 'inscripcion')
        verbose_name = 'Calificación de Actividad'
        verbose_name_plural = 'Calificaciones de Actividades'

    def __str__(self):
        return f"{self.actividad.nombre} - {self.inscripcion.alumno}: {self.calificacion or 'Sin calificar'}"


class Kardex(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name='kardex')
    calificacion_final = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Kardex'
        verbose_name_plural = 'Kardex'

    def __str__(self):
        return f"Kardex de {self.inscripcion.alumno} para {self.inscripcion.curso}"

    def calcular_promedio(self):
        """
        Calcula el promedio de todas las actividades calificadas.
        """
        calificaciones = self.inscripcion.calificaciones_actividades.filter(
            calificacion__isnull=False
        )
        if not calificaciones.exists():
            return None
        
        total = sum(calif.calificacion for calif in calificaciones)
        return total / calificaciones.count()
