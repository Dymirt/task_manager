# Generated by Django 4.1.4 on 2023-01-07 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0003_alter_member_organization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]