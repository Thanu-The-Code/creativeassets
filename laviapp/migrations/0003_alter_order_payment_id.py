# Generated by Django 4.2.14 on 2025-01-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laviapp', '0002_alter_categoryvideo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
