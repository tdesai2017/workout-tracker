# Generated by Django 2.1.7 on 2019-04-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_info_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
