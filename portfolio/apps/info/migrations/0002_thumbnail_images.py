# Generated by Django 4.1.3 on 2022-11-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='images',
            field=models.ImageField(default='', upload_to='project/thumbnail'),
            preserve_default=False,
        ),
    ]
