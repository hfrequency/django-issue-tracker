from django.conf.urls.defaults import *
from core.views import projects, project_detail

urlpatterns = patterns('',
    (r'^projects/$', projects, {}, 'projects' ),
    (r'^projects/(?P<project_id>\d+)/$', project_detail, {}, 'project_detail' ),
)

