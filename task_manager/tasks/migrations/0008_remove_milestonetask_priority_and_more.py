# Generated by Django 4.1.4 on 2023-01-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0007_alter_daytask_priority_alter_daytask_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="milestonetask",
            name="priority",
        ),
        migrations.RemoveField(
            model_name="milestonetask",
            name="status",
        ),
        migrations.AddField(
            model_name="milestonetask",
            name="complete",
            field=models.BooleanField(default=False),
        ),
    ]
