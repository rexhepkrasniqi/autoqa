# Generated by Django 4.1.3 on 2022-11-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='content',
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
    ]
