# Generated by Django 3.2.20 on 2023-08-01 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationpost',
            name='img_file',
        ),
        migrations.RemoveField(
            model_name='publicationpost',
            name='pb_author',
        ),
        migrations.RemoveField(
            model_name='publicationpost',
            name='pb_author_url',
        ),
    ]
