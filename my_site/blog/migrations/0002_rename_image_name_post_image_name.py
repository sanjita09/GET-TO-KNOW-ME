# Generated by Django 3.2.3 on 2021-05-21 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_Name',
            new_name='image_name',
        ),
    ]
