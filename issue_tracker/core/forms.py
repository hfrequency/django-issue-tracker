from django.forms import ModelForm
from issue_tracker.core.models import Project, Issue

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'version', 'release_date')

class IssueForm(ModelForm):
    class Meta:
        model = Issue
