# Generated by Django 3.0.1 on 2020-01-09 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0036_studentuploadfile_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuploadfile',
            old_name='assignment',
            new_name='student_upload',
        ),
    ]
