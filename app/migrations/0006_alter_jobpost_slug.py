# Generated by Django 4.1.2 on 2022-10-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_jobpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
