from django.db import models
from django.contrib.auth.models import AbstractUser


ON_HOLD = "OH"
NOT_STARTED = "NS"
IN_PROGRESS = "IP"
COMPLETED = "C"
STATUS_CHOICES = [
    (ON_HOLD, "Wstrzymane"),
    (NOT_STARTED, "Nie rozpoczęte"),
    (IN_PROGRESS, "W trakcie"),
    (COMPLETED, "Zakończone"),
]

LOW = "L"
HIGH = "H"
PRIORITY_CHOICES = [
    (LOW, "Niski"),
    (HIGH, "Wysoki"),
]


class User(AbstractUser):
    organization = models.ForeignKey(
        "Organization",
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )


class Project(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    members = models.ManyToManyField("User", related_name="project_members", blank=True)
    author = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="project_authored"
    )
    organization = models.ForeignKey(
        "Organization",
        on_delete=models.CASCADE,
        related_name="projects",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def completion(self):
        return round(
            self.project_tasks.filter(status=COMPLETED).count()
            / self.project_tasks.all().count()
            * 100
        )


class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="project_tasks"
    )
    assignment = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="tasks_assignments",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="tasks_authored"
    )

    def __str__(self):
        return f"{self.priority} - {self.title}"


class DayTask(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="day_tasks")
    title = models.CharField(max_length=64)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    parent = models.ForeignKey(
        "DayTask",
        on_delete=models.CASCADE,
        related_name="childs",
        null=True,
        blank=True,
    )


class Organization(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
