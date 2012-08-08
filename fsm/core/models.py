# -*- coding: utf-8 -*-
from django.db import models

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from datetime import datetime


class Technician(models.Model):
    CONNECTION_TYPE = [
        ('1', _(u'on-line')),
        ('2', _(u'off-line')),
    ]
    CONNECTION_TYPE_AND_EMPTY = [('','---------')] + CONNECTION_TYPE

    name = models.CharField(max_length=255, verbose_name=_(u'Nome'))
    connection_type = models.CharField(max_length=1, choices=CONNECTION_TYPE, verbose_name=_(u'Conexão'))
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=_(u'Usuário'))

    class Meta:
        ordering = ['user']
        verbose_name = _(u'Técnico')
        verbose_name_plural = _(u'Técnicos')

    def __unicode__(self):
        return self.name

class TaskType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Nome'))

    class Meta:
        verbose_name = _(u'Tipo de Tarefa')
        verbose_name_plural = _(u'Tipos de Tarefas')

    def __unicode__(self):
        return self.name

class Task(models.Model):
    STATUS = [
        ('1', _(u'Criada')),
        ('2', _(u'Asignada')),
        ('3', _(u'Suspensa')),
        ('4', _(u'Concluída')),
    ]
    STATUS_AND_EMPTY = [('','---------')] + STATUS

    name = models.CharField(max_length=255, verbose_name=_(u'Nome'))
    description = models.CharField(max_length=255, verbose_name=_(u'Descrição'))
    task_type = models.ForeignKey(TaskType, verbose_name=_(u'Tipo'))
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=_(u'Status'))
    create_date = models.DateTimeField(verbose_name=_(u'Data de criação'), default=datetime.now)
    last_update = models.DateTimeField(verbose_name=_(u'Última Atualização'), default=datetime.now)

    class Meta:
        verbose_name = _(u'Tarefa')
        verbose_name_plural = _(u'Tarefas')

    def __unicode__(self):
        return self.name
