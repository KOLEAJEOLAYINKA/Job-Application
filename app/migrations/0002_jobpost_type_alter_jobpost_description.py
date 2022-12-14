# Generated by Django 4.1.1 on 2022-11-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="type",
            field=models.CharField(
                choices=[("Full Time", "Full Time"), ("Part Time", "Part Time")],
                default="Full Time",
                max_length=200,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="description",
            field=models.TextField(),
        ),
    ]
