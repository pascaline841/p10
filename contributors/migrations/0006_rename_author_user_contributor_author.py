# Generated by Django 3.2.4 on 2021-07-06 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contributors", "0005_alter_contributor_permission"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contributor",
            old_name="author",
            new_name="author",
        ),
    ]
