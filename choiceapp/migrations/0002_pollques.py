# Generated by Django 4.1 on 2022-08-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choiceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pollques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(max_length=280)),
                ('cho1', models.CharField(max_length=30)),
                ('cho2', models.CharField(max_length=30)),
                ('cho3', models.CharField(max_length=30)),
                ('cho4', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('t_time', models.CharField(max_length=15)),
                ('t_date', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'poll_ques',
            },
        ),
    ]
