from django.conf.urls.defaults import *
from core.views import projects, issues 

urlpatterns = patterns('',
    (r'^projects/$', projects, {}, 'projects' ),
    (r'^issues/(?P<project_id>\d+)/$', issues, {}, 'issues' ),
    (r'^comments/(?P<issue_id>\d+)/$', comments, {}, 'comments' ),
)

