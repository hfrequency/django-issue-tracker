from django.conf.urls.defaults import *
from core.views import projects, issues, comments 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^projects/$', projects, {}, 'projects' ),
    (r'^issues/(?P<project_id>\d+)/$', issues, {}, 'issues' ),
    (r'^comments/(?P<project_id>\d+)/(?P<issue_id>\d+)/$', comments, {}, 'comments' ),
)

urlpatterns += staticfiles_urlpatterns()
