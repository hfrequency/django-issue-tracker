from django.conf.urls.defaults import *
from core.views import issues

urlpatterns = patterns('',
    (r'^issues/$', issues, {}, 'issues' ),
)

