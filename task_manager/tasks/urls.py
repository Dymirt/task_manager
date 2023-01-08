from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/<str:username>", views.profile_view, name="profile"),
    path("billing/", views.billing_view, name="billing"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("notification/", views.notification_view, name="notification"),
    path("map/", views.map_view, name="map"),
    path("tables/", views.tables_view, name="tables"),
    path("template/", views.template_view, name="template"),
    path("typography/", views.typography_view, name="typography"),
    path("virtual/", views.virtual_view, name="virtual"),
    path("projects/", views.projects_view, name="projects"),
    path("project/<int:project_id>", views.project_detail_view, name="project"),
    # Project PUT
    path("project/<int:project_id>/status/put", views.project_put_status),
    path("project/<int:project_id>/priority/put", views.project_put_priority),
    path("project/<int:project_id>/member/put", views.project_put_member),
    path("project/<int:project_id>/add-project-task", views.add_project_task, name='add_project_task'),
    # Tasks PUT
    path("task/<int:task_id>/status/put", views.task_put_status),
    path("task/<int:task_id>/priority/put", views.task_put_priority),
    path("task/<int:task_id>/assignment/put", views.task_put_assignment),
    path("task/<int:task_id>/remove", views.task_remove),
]
