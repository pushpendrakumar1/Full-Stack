# Generated by Django 4.2 on 2023-06-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_activitylists_activity_activitylists_added_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylists',
            name='G_IX_date',
            field=models.TextField(),
        ),
    ]
