# Generated by Django 4.2.7 on 2023-11-14 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_alter_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='group',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]