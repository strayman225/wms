# Generated by Django 3.2.23 on 2023-11-28 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20231128_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transdate', models.DateTimeField(auto_now_add=True)),
                ('qtyIN', models.PositiveIntegerField(default=0)),
                ('qtyout', models.PositiveIntegerField(default=0)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.stock')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse')),
            ],
        ),
    ]
