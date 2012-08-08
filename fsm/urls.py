from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'fsm.views.home', name='home'),
    # User profile
    url(r'^accounts/profile/$', 'fsm.views.profile', name='profile'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Login
    (r'^login/$', 'django.contrib.auth.views.login'),
    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Core app
    (r'^', include('fsm.core.urls', namespace='core')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    # Defining URL mapping in the static files for environment Heroku
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
            'document_root': settings.STATIC_ROOT,
            'insecure': True}),
    )

