# Generated by Django 3.0 on 2019-12-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_photos_photographer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]