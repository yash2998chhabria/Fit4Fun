# Generated by Django 2.2 on 2020-10-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201012_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='video_5',
            field=models.CharField(default='', max_length=500),
        ),
    ]
