# Generated by Django 3.2.15 on 2023-06-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mksd', '0016_alter_neuigkeit_neu_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuigkeit',
            name='neu_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
