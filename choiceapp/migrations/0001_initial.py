# Generated by Django 4.1 on 2022-08-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=180)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=55)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]