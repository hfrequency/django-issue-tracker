from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, login
from accounts.views import register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
    (r'^register/$', register, {}, 'register' ),
    (r'^login/$', login, {}, 'login' ),
        (r'^logout/$', logout_then_login, {'login_url':'/login/'}, 'logout'),
)
