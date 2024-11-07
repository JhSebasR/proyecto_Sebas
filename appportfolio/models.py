# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import user
from django.db import models


################################################
# 1 - Categoria
################################################
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField('Puesto de Trabajo',max_length=30,null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria' #puede ser otro nombre
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria']

    def __str__(self):
        return "%s,%s" % (self.id,self.nombre_categoria)

################################################
# 2 - Experiencias
################################################
class Experiencia(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField('Empresa',max_length=50,null=True, blank=True)
    fecha_inicio= models.DateField('Fecha de Inicio',null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    observaciones = models.CharField('Funciones', max_length=50, null=True, blank=True)
    categoria = models.CharField(Categoria,max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Experiencia' #puede ser otro nombre
        verbose_name_plural = 'Experiencias'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id,self.empresa,self.fecha_inicio,self.fecha_fin,self.observaciones,self.categoria)



################################################
# 3 - Estudios
################################################
class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    titulacion = models.CharField('titulacion',max_length=50,null=True, blank=True)
    edad = models.IntegerField()
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    nota = models.IntegerField('Nota', null=True, blank=True)
    lugarEstudio = models.CharField('Lugar Estudio', max_length=50, null=True, blank=True)
    presencial = models.BooleanField('Presencial', null=True, blank=True)
    observaciones = models.CharField('obsevaciones', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Estudio' #puede ser otro nombre
        verbose_name_plural = 'Estudios'
        ordering = ['titulacion']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id,self.titulacion,self.edad,self.fecha_inicio,self.fecha_fin,self.nota,self.lugarEstudio,self.presencial,self.observaciones)

################################################
# 4 - Habilidades
################################################
class Habilidad(models.Model):
    id = models.AutoField(primary_key=True)
    habilidad = models.CharField('Habilidad',max_length=30,null=True, blank=True)
    nivel = models.CharField('nivel', max_length=30, null=True, blank=True)
    Comentario = models.CharField('Comentario', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Habilidad' #puede ser otro nombre
        verbose_name_plural = 'Habilidades'
        ordering = ['habilidad']

    def __str__(self):
        return "%s,%s,%s,%s" % (self.id,self.habilidad,self.nivel,self.Comentario)


usuario = models.ForeignKey(User, related_name='datos_usuario', null=True, blank=True, on_delete= models.PROTECT)

################################################
# 5 - Imagen
################################################
class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField('Imagen',blank=True,null=True, upload_to="imagenes/")
    comentario = models.CharField('Comentario', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Imagen' #puede ser otro nombre
        verbose_name_plural = 'Imagenes'
        ordering = ['id']

    def __str__(self):
        return "%s,%s,%s" % (self.id,self.imagen,self.Comentario)