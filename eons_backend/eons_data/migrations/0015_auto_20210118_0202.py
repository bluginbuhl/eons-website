# Generated by Django 3.1.5 on 2021-01-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eons_data', '0014_auto_20210118_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eonsbasedata',
            options={'verbose_name': 'EONS Datum', 'verbose_name_plural': 'EONS Data'},
        ),
        migrations.AddField(
            model_name='eonsbasedata',
            name='local_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
