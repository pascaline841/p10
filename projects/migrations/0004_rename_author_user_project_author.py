# Generated by Django 3.2.4 on 2021-07-06 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_rename_author_user_id_project_author_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="author",
            new_name="author",
        ),
    ]
