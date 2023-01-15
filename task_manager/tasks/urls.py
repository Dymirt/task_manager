from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/<str:username>", views.profile_view, name="profile"),
    path("billing/", views.billing_view, name="billing"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("notification/", views.notification_view, name="notification"),
    path("tables/", views.tables_view, name="tables"),
    path("template/", views.template_view, name="template"),
    path("typography/", views.typography_view, name="typography"),
    # Project
    path("projects/", views.projects_view, name="projects"),
    path("project/<int:project_id>", views.project_detail_view, name="project"),
    path("project/<int:project_id>/status/put", views.project_put_status),
    path("project/<int:project_id>/priority/put", views.project_put_priority),
    path("project/<int:project_id>/member/put", views.project_put_member),
    path("project/<int:project_id>/add-project-milestone", views.add_project_milestone, name='add_project_milestone'),
    # Milestone
    path("milestone/<int:milestone_id>/status/put", views.milestone_put_status),
    path("milestone/<int:milestone_id>/priority/put", views.milestone_put_priority),
    path("milestone/<int:milestone_id>/assignment/put", views.milestone_put_assignment),
    path("milestone/<int:milestone_id>/remove", views.milestone_remove),
    path("milestone/<int:milestone_id>/tasks", views.milestone_tasks, name='milestone_tasks'),
    path("milestone/<int:milestone_id>/tasks/add", views.milestone_tasks_add, name='milestone_task_add'),

]
