# Generated by Django 4.2 on 2023-05-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('secondname', models.CharField(max_length=255)),
                ('companyname', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('roleid', models.IntegerField()),
            ],
        ),
    ]
