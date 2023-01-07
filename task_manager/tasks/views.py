from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import User, Project, Task, Organization, STATUS_CHOICES, PRIORITY_CHOICES
from django.db import IntegrityError
import json
from .forms import OrganizationLoginForm

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
            return render(
                request,
                "tasks/pages/sign-in.html",
                {"message": "Invalid username and/or password."},
            )
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
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "tasks/pages/sign-up.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tasks/pages/sign-up.html")


def index(request):
    return render(request, "tasks/index.html")


@login_required
def profile_view(request):

    form = OrganizationLoginForm()
    context = {
        "form": form,
        "status_choices": STATUS_CHOICES,
        "priority_choices": PRIORITY_CHOICES,
    }

    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            try:
                organization = Organization.objects.get(title=form.cleaned_data.get('title'))
            except Organization.DoesNotExist:
                context['organization_form_message'] = "Invalid username and/or password."
                return render(request, "tasks/pages/profile.html", context=context)
            if organization.password == form.cleaned_data.get('password'):
                member = request.user.member
                member.organization = organization
                member.save()
            else:
                return render(request, "tasks/pages/profile.html", context=context)



    return render(request, "tasks/pages/profile.html", context=context)


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


@login_required
def projects_view(request):
    try:
        projects = request.user.organization.projects.all()
    except AttributeError as e:
        projects = []
    context = {
        "projects": projects,
        "status_choices": STATUS_CHOICES,
        "priority_choices": PRIORITY_CHOICES,
    }
    return render(request, "tasks/pages/projects.html", context=context)


@login_required
def project_detail_view(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.user in project.organization.users.all():
        context = {
            "project": project,
            "status_choices": STATUS_CHOICES,
            "priority_choices": PRIORITY_CHOICES,
        }
        return render(request, "tasks/pages/project_detail.html", context=context)


def add_project_task(request, project_id):
    if request.method == "POST":
        task = Task.objects.create(title=request.POST['title'],
                                   deadline=request.POST['deadline'],
                                   status=request.POST['status'],
                                   priority=request.POST['priority'],
                                   project=Project.objects.get(pk=project_id),
                                   assignment=User.objects.get_by_natural_key(request.POST['assignment']),
                                   author=request.user
                                   )
        task.save()

    return HttpResponseRedirect(reverse("project", args=[project_id]))


#################
# Project PUT views
#################


@login_required
def project_put_status(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user == project.author:
        if request.method == "PUT":
            data = json.loads(request.body)
            project.status = data["status"]
            project.save()
            return HttpResponse(status=204)


@login_required
def project_put_priority(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user == project.author:
        if request.method == "PUT":
            data = json.loads(request.body)
            project.priority = data["priority"]
            project.save()
            return HttpResponse(status=204)


@login_required
def project_put_member(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user == project.author:
        if request.method == "PUT":
            data = json.loads(request.body)
            member = User.objects.get_by_natural_key(data["member"])
            if member in project.members.all():
                project.members.remove(member)
            else:
                project.members.add(member)

            return HttpResponse(status=204)


#################
# Tasks PUT views
#################


@login_required
def task_put_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        task.status = data["status"]
        task.save()
        return HttpResponse(status=204)


@login_required
def task_put_priority(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        task.priority = data["priority"]
        task.save()
        return HttpResponse(status=204)


@login_required
def task_put_assignment(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        if data["assignment"] != "None":
            member = User.objects.get_by_natural_key(data["assignment"])
            task.assignment = member
        else:
            task.assignment = None
        task.save()
        return HttpResponse(status=204)


@login_required
def task_remove(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "DELETE":
        task.delete()
        return HttpResponse(status=204)


#################
# Tasks PUT views
#################