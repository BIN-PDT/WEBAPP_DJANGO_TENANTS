# Generated by Django 5.1.7 on 2025-03-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0002_sitesetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
