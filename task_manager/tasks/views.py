from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import User, Project, Task, STATUS_CHOICES, PRIORITY_CHOICES
from django.db import IntegrityError
from .forms import ProjectAssignmentForm, ProjectStatusForm
import json



# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/pages/sign-in.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tasks/pages/sign-in.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tasks/pages/sign-up.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tasks/pages/sign-up.html")


def index(request):
    return render(request, "tasks/index.html")

@login_required
def profile_view(request):
    return render(request, "tasks/pages/profile.html")


def dashboard_view(request):
    return render(request, "tasks/pages/dashboard.html")


def billing_view(request):
    return render(request, "tasks/pages/billing.html")


def icons_view(request):
    return render(request, "tasks/pages/icons.html")


def map_view(request):
    return render(request, "tasks/pages/map.html")


def tables_view(request):
    return render(request, "tasks/pages/tables.html")


def template_view(request):
    return render(request, "tasks/pages/template.html")


def virtual_view(request):
    return render(request, "tasks/pages/virtual-reality.html")


def typography_view(request):
    return render(request, "tasks/pages/typography.html")


class ProjectsListView(ListView):
    template_name = "tasks/pages/projects.html"
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        project_status_form = ProjectStatusForm()
        context['priority_choices'] = PRIORITY_CHOICES
        context['status_choices'] = STATUS_CHOICES

        return context


def project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    assignment_form = ProjectAssignmentForm(instance=project)
    status_form = ProjectStatusForm(instance=project)

    context = {'project': project,
               'assignment_form': assignment_form,
               'status_form': status_form,
               'status_choices': STATUS_CHOICES,
               'priority_choices': PRIORITY_CHOICES,
               }

    return render(request, "tasks/pages/project_detail.html", context=context)


def project_assignment(request, project_id):
    if request.method == "POST":
        project = Project.objects.get(pk=project_id)
        form = ProjectAssignmentForm(request.POST, instance=project)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('project', project_id)


def project_put_status(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        project.status = data["status"]
        project.save()
        return HttpResponse(status=204)


def project_put_priority(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        project.priority = data["priority"]
        project.save()
        return HttpResponse(status=204)


def task_put_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        task.status = data["status"]
        task.save()
        return HttpResponse(status=204)



