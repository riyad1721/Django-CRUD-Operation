# Generated by Django 4.0.6 on 2022-10-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rool', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
