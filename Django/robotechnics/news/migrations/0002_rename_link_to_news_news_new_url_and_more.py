# Generated by Django 4.2.6 on 2023-11-23 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='link_to_news',
            new_name='new_url',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name',
            new_name='title',
        ),
    ]
