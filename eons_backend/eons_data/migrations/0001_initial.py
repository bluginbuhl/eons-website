# Generated by Django 3.1.1 on 2020-09-27 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EonsSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_code', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['site_code'],
            },
        ),
    ]