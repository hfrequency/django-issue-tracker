from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from core.models import *

@login_required(login_url='/login/')
def issues(request):
    projects = Project.objects.all() 
    return render_to_response("projects.html", {
        'projects' : projects,
    })
