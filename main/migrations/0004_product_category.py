# Generated by Django 5.1.1 on 2024-09-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
