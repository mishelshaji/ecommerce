# Generated by Django 3.1.5 on 2021-01-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Category Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
            ],
        ),
    ]
