# Generated by Django 4.1.4 on 2023-01-01 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_project_members"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="project",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="project_members", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="tasks.organization",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="tasks.organization",
            ),
        ),
    ]
