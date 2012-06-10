from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Examples:
    (r'^$', 'direct_to_template', {
        'template': 'index.html'
    }),
   
    url(r'^', include('core.urls')),
    url(r'^', include('accounts.urls')),
    # url(r'^$', 'issue_tracker.views.home', name='home'),
    # url(r'^issue_tracker/', include('issue_tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
