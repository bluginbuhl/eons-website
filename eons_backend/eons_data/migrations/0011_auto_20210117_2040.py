# Generated by Django 3.1.2 on 2021-01-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eons_data', '0010_auto_20210117_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eonscsv',
            name='file_name',
            field=models.FileField(upload_to='eons_csvs/<function site_folder at 0x7fd744e75e50>/'),
        ),
    ]