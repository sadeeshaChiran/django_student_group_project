# Generated by Django 4.2.7 on 2023-11-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]