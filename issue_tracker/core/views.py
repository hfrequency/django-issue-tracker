from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from core.models import *

@login_required(login_url='/login/')
def projects(request):
    projects = Project.objects.all() 
    return render_to_response("projects.html", {
        'projects' : projects,
    })

@login_required(login_url='/login/')
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id) 
    return render_to_response("projects.html", {
        'project' : project,
    })
