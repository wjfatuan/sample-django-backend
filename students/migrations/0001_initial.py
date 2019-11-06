# Generated by Django 2.2.6 on 2019-10-16 01:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Code assigned to the student', max_length=12)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', help_text='Gender', max_length=1)),
                ('first_name', models.CharField(help_text='First name', max_length=20)),
                ('last_name', models.CharField(help_text='Last name', max_length=20)),
                ('birth_date', models.DateField(default=datetime.date.today, help_text='Birth date')),
                ('phone_number', models.CharField(blank=True, help_text='Phone number', max_length=12)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('HOME', 'Home'), ('Work', 'Work'), ('FAMILY', 'Family')], help_text='Address type', max_length=12)),
                ('address', models.CharField(help_text='Address', max_length=100)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
