from django.forms import ModelForm
from .models import Project


class ProjectAssignmentForm(ModelForm):
    class Meta:
        model = Project
        fields = ["members"]


class ProjectStatusForm(ModelForm):
    class Meta:
        model = Project
        fields = ["status"]

    def __init__(self, *args, **kwargs):
        super(ProjectStatusForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs[
            "onchange"
        ] = "put_project_status(this.value)"
