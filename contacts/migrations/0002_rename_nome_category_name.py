# Generated by Django 4.1.3 on 2022-11-14 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nome',
            new_name='name',
        ),
    ]
