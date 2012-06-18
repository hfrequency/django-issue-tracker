from django.forms import ModelForm, Textarea
from issue_tracker.core.models import Project, Issue, Comments

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'version', 'release_date')

class IssueForm(ModelForm):
    class Meta:
        model = Issue

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
