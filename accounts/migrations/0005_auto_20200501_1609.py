# Generated by Django 3.0.5 on 2020-05-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200501_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(default='user.png', upload_to='user_image'),
        ),
    ]