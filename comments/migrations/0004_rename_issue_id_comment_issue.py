# Generated by Django 3.2.4 on 2021-06-22 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_rename_author_user_id_comment_author_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
    ]
