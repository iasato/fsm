from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('fsm.core.views',
    url(r'^technician/$', 'technician_add', name='technician_add'),
    url(r'^technician/(\d+)$', 'technician', name='technician'),
    url(r'^technician_search/$', 'technician_search', name='technician_search'),
    url(r'^technician_results/$', 'ajax_technician_search', name='ajax_technician_search'),
    url(r'^task_search/$', 'task_search', name='task_search'),
    url(r'^task_results/$', 'ajax_task_search', name='ajax_task_search'),
)
