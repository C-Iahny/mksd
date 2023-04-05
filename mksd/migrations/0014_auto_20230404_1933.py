# Generated by Django 3.2.2 on 2023-04-04 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mksd', '0013_alter_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/reglo_photo'),
        ),
    ]
