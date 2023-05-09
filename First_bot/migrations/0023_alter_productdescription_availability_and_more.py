# Generated by Django 4.2.1 on 2023-05-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_bot', '0022_remove_productdescription_compatible_device_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescription',
            name='availability',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='brand',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='total_rating',
            field=models.CharField(blank=True, default=0, max_length=25, null=True),
        ),
    ]
