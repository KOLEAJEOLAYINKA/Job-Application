# Generated by Django 4.1.2 on 2022-11-01 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_jobpost_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobpost",
            old_name="slug",
            new_name="url",
        ),
    ]
