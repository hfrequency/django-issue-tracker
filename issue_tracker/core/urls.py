from django.conf.urls.defaults import *
from core.views import projects 

urlpatterns = patterns('',
    (r'^projects/$', projects, {}, 'projects' ),
)

