# Generated by Django 3.1.5 on 2021-01-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eons_data', '0004_auto_20210123_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eonsbasedata',
            name='utc_datetime',
            field=models.DateTimeField(verbose_name='UTC datetime'),
        ),
    ]
