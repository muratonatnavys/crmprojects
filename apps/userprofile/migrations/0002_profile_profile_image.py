# Generated by Django 3.1.2 on 2020-10-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='users/'),
        ),
    ]
