# Generated by Django 5.0 on 2023-12-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
