# Generated by Django 2.2.13 on 2020-08-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200823_0532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.AddField(
            model_name='experience',
            name='Comment_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experience',
            name='Comment_2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experience',
            name='Comment_3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experience',
            name='Comment_4',
            field=models.TextField(default=''),
        ),
    ]
