# Generated by Django 3.2.23 on 2023-12-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0016_transaction_docnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='qtyIN',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='qtyout',
            field=models.IntegerField(default=0),
        ),
    ]
