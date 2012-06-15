from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import *
from django.forms.models import modelformset_factory, inlineformset_factory
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from core.forms import *

@login_required(login_url='/login/')
@csrf_protect
def projects(request):

    project = Project.objects.all()

    # TODO check if this is the best way to get the current user in session.
    user = User.objects.get(username=request.META["USER"])

    ProjectFormSet = inlineformset_factory(User, Project, max_num=10, extra=1, \
        fields = ('name', 'version', 'release_date'))
        

    if request.method == 'POST':
        formset = ProjectFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/projects/')
    else:
        formset = ProjectFormSet(instance=user) 

    return render_to_response("projects.html", {
        'formset' : formset
    }, context_instance=RequestContext(request))

