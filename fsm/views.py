# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)

@login_required(login_url='/login/')
def profile(request):
    return HttpResponseRedirect(reverse('home'))
