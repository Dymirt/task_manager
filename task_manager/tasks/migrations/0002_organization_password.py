# Generated by Django 4.1.4 on 2023-01-07 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="password",
            field=models.CharField(max_length=32, null=True),
        ),
    ]
