from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, login
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
    (r'^login/$', login, {'authentication_form': AuthenticationForm}, 'login'),
        (r'^logout/$', logout_then_login, {}, 'logout'),
)
