# Generated by Django 4.2.13 on 2024-06-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_num', models.IntegerField(unique=True)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]