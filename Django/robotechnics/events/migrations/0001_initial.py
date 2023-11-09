# Generated by Django 4.2.6 on 2023-11-09 13:18

from django.db import migrations, models
import django.db.models.deletion
import events.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassicEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('link_to_photo_album', models.URLField(verbose_name='ссылка на фото-фльбом')),
                ('link_to_the_docs', models.URLField(verbose_name='ссылка на документы')),
                ('venue', models.URLField(verbose_name='место проведения')),
                ('date_of_the_event', models.DateField(verbose_name='дата проведения')),
                ('mention_in_the_media', models.URLField(verbose_name='упоминание в сми')),
                ('link_to_the_registr', models.URLField(verbose_name='ссылка на регистрацию')),
                ('partners', models.ManyToManyField(to='partners.partner', verbose_name='партнёры классического мероприятия')),
            ],
            options={
                'verbose_name': 'классическое мероприятие',
                'verbose_name_plural': 'классические мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, validators=[events.validators.ValidateFullName()], verbose_name='фио участника')),
                ('group', models.CharField(max_length=15, validators=[events.validators.ValidateGroup()], verbose_name='учебная группа')),
                ('number_of_people', models.IntegerField(verbose_name='количество людей в команде')),
                ('required_competencies', models.TextField(verbose_name='необходимые компетенции')),
                ('link_to_vk', models.URLField(verbose_name='ссылка на ВКонтакте соискателя')),
                ('additional_information', models.TextField(verbose_name='дополнительная информация')),
                ('classic_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.classicevent', verbose_name='классическое мероприятие')),
            ],
            options={
                'verbose_name': 'анкета',
                'verbose_name_plural': 'анкеты',
            },
        ),
    ]
