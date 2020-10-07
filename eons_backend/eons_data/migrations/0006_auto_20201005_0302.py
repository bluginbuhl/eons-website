# Generated by Django 3.1.1 on 2020-10-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eons_data', '0005_auto_20201005_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eonssite',
            name='users',
        ),
        migrations.AddField(
            model_name='eonssite',
            name='users',
            field=models.ManyToManyField(related_name='_eonssite_users_+', to='eons_data.EonsSite'),
        ),
    ]
