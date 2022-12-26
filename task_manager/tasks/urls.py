from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path('profile/', views.profile_view, name='profile'),
    path("billing/", views.billing_view, name="billing"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('icons/', views.icons_view, name='icons'),
    path('map/', views.map_view, name='map'),
    path('tables/', views.tables_view, name='tables'),
    path('template/', views.template_view, name='template'),
    path('typography/', views.typography_view, name='typography'),
    path('virtual/', views.virtual_view, name='virtual'),
    path('projects/', views.ProjectsListView.as_view(), name='projects'),
    path("project/<int:project_id>", views.project_view, name="project"),
    path('project/<int:project_id>/assignment/', views.project_assignment, name="project_assignment"),
    path('project/<int:project_id>/status/put', views.project_put_status),
    path('project/<int:project_id>/priority/put', views.project_put_priority),

    path('task/<int:task_id>/status/put', views.task_put_status, name="task_status")

]