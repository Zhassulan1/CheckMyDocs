# Generated by Django 5.0.4 on 2024-05-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_uploadedfile_doc_type_uploadedfile_file_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadedFile',
            new_name='FileData',
        ),
    ]
