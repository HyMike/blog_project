# Generated by Django 5.0.1 on 2024-02-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0007_post_upload_images_alter_post_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="upload_images",
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="post"),
        ),
    ]
