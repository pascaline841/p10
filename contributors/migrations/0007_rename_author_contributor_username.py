# Generated by Django 3.2.4 on 2021-07-08 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0006_rename_author_user_contributor_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='author',
            new_name='username',
        ),
    ]
