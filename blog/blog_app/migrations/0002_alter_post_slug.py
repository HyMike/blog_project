# Generated by Django 5.0.1 on 2024-02-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, default="", null=True),
        ),
    ]
