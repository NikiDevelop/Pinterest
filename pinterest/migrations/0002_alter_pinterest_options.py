# Generated by Django 4.0 on 2023-10-05 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pinterest',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
