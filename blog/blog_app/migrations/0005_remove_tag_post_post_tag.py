# Generated by Django 5.0.1 on 2024-02-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0004_post_author_tag_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="post",
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(to="blog_app.tag"),
        ),
    ]
