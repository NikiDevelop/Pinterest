# Generated by Django 4.2.6 on 2023-10-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0002_alter_pinterest_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinterest',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]