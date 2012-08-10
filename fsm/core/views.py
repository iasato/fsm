# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from models import Technician, Task
from forms import TechnicianForm, TechnicianSearchForm, TaskSearchForm


@login_required(login_url='/login/')
def technician_add(request):
    if request.method == 'POST':
        return technician_create(request)
    else:
        return technician_new(request)

def technician_new(request):
    form = TechnicianForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('core/technician_add.html', context)

def technician_create(request):
    form = TechnicianForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('core/technician_add.html', context)

    form.save()

    return HttpResponseRedirect(
        reverse('core:technician_search'))

@login_required(login_url='/login/')
def technician(request, pk):
    t = get_object_or_404(Technician, pk=pk)
    context = RequestContext(request, {'technician': t})
    return render_to_response('core/technician.html', context)

@login_required(login_url='/login/')
def technician_search(request):
    form = TechnicianSearchForm(auto_id=True)

    context = RequestContext(request)
    return render_to_response('core/technician_search.html',
                            {'form': form},
                             context)

@login_required(login_url='/login/')
def ajax_technician_search(request):
    if request.is_ajax():
        query = (Q(name__icontains=request.GET.get('technician')))
        query = query & (Q(connection_type__icontains=request.GET.get('connection_type')))

        results = Technician.objects.filter(query).distinct().order_by('name')

        template = 'core/technician_result.html'
        data = {
            'results': results,
        }
        context = RequestContext(request)

        return render_to_response(template, data, context)

@login_required(login_url='/login/')
def task_search(request):
    form = TaskSearchForm(auto_id=True)

    context = RequestContext(request)
    return render_to_response('core/task_search.html',
                            {'form': form},
                             context)

@login_required(login_url='/login/')
def ajax_task_search(request):
    if request.is_ajax():
        query = (Q(name__icontains=request.GET.get('task')))
        query = query & (Q(task_type__id__icontains=request.GET.get('task_type')))
        query = query & (Q(status__icontains=request.GET.get('status')))

        results = Task.objects.filter(query).distinct().order_by('name')
        print results

        template = 'core/task_result.html'
        data = {
            'results': results,
        }
        context = RequestContext(request)

        return render_to_response(template, data, context)
