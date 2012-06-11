from django.conf.urls.defaults import *
from core.views import issues

urlpatterns = patterns('',
    (r'^projects/(?P<project_id>\d+)/$', projects, {}, 'projects' ),
)

