# Generated by Django 2.2.5 on 2022-01-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_vehicles_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='username',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
