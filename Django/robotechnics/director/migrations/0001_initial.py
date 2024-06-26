# Generated by Django 4.2.6 on 2023-11-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('post', models.CharField(max_length=150, verbose_name='должность')),
            ],
            options={
                'verbose_name': 'руководитель',
                'verbose_name_plural': 'руководители',
            },
        ),
    ]
