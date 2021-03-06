# Generated by Django 3.2 on 2021-07-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('Organizer', models.CharField(max_length=50)),
                ('qualifications', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='activity2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('Organizer', models.CharField(max_length=50)),
                ('qualifications', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'activity2',
            },
        ),
    ]
