# Generated by Django 3.2.20 on 2023-08-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0007_publicationpost_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationpost',
            name='author',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
