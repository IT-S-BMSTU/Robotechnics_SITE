# Generated by Django 4.2.6 on 2023-11-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_link_to_news_news_new_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='photo',
        ),
    ]
