# Generated by Django 3.2.23 on 2023-11-28 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0013_stock_coding'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock',
            new_name='Items',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='stock',
            new_name='item',
        ),
    ]