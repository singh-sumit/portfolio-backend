# Generated by Django 4.1.3 on 2022-11-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_technology_image_height_technology_image_width_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='tech/icons/'),
        ),
    ]
