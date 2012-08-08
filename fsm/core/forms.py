# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from models import Technician, Task, TaskType


class TechnicianSearchForm(forms.Form):
    technician = forms.CharField(label=_(u"Técnico"),
                            widget=forms.TextInput(attrs={'class': 'span3'}))
    connection_type = forms.ChoiceField(label=_(u"Tipo de Conexão"),
                            choices=Technician.CONNECTION_TYPE_AND_EMPTY,
                            widget=forms.Select(attrs={'class': 'span2'}))

class TaskSearchForm(forms.Form):
    task = forms.CharField(label=_(u"Tarefa"),
                            widget=forms.TextInput(attrs={'class': 'span3'}))
    task_type = forms.ModelChoiceField(label=_(u"Tipo de Tarefa"),
                            queryset=TaskType.objects.all(),
                            widget=forms.Select(attrs={'class': 'span3'}))
    status = forms.ChoiceField(label=_(u"Status"), choices=Task.STATUS_AND_EMPTY,
                            widget=forms.Select(attrs={'class': 'span2'}))
