# Generated by Django 3.1.7 on 2021-03-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='fb_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='insta_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
