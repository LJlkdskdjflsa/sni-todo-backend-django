# Generated by Django 3.1 on 2021-09-07 00:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'task catogory',
                'verbose_name_plural': 'task catogories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('estimated_time', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.category')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'task',
            },
        ),
    ]
