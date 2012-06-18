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


@login_required(login_url='/login/')
@csrf_protect
def issues(request, project_id):
    # TODO check if this is the best way to get the current user in session.
    user = User.objects.get(username=request.META["USER"])
    project = Project.objects.get(id=project_id)

    IssuesFormSet = inlineformset_factory(Project, Issue, max_num=10, extra=1, \
        fields = ('status', 'level', 'title', 'description'))

    if request.method == 'POST':
        formset = IssuesFormSet(request.POST, instance=project)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/issues/%s' % project_id)
    else:
        formset = IssuesFormSet(instance=project)

    return render_to_response("issues.html", {
        'formset' : formset,
        'project_id' : project_id
    }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@csrf_protect
def comments(request, project_id, issue_id):
    # TODO check if this is the best way to get the current user in session.
    user = User.objects.get(username=request.META["USER"])
    issue = Issue.objects.get(id=issue_id)

    CommentsFormSet = inlineformset_factory(Issue, Comments, max_num=10, extra=1, fields=['user', 'comment'], can_delete=True)

    if request.method == 'POST':
        formset = CommentsFormSet(request.POST, instance=issue)
        if formset.is_valid():
            comment = formset.save(commit=False)
            # we only want to update the new record (which is always the last
            # form)
            comment[-1].user = request.user
            comment[-1].save()
            formset.save()
            return HttpResponseRedirect('/comments/%s/%s' % (project_id, issue_id) )
    else:
        formset = CommentsFormSet(instance=issue)

    return render_to_response("comments.html", {
        'formset' : formset,
        'project_id' : project_id,
        'issue_id' : issue_id
    }, context_instance=RequestContext(request))

