# Generated by Django 4.1.3 on 2022-11-02 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('status', models.CharField(choices=[('success', 'Success'), ('failed', 'Failed'), ('unknown', 'Unknown')], default='unknown', max_length=30)),
                ('type', models.CharField(choices=[('api', 'API reader'), ('selenium', 'Selenium task')], default='selenium', max_length=30)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(blank=True, max_length=300, null=True)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True)),
                ('target', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.action')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.task')),
            ],
        ),
    ]