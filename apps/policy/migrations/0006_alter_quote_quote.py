# Generated by Django 3.2.3 on 2021-06-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0005_auto_20210602_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=20, unique=True, verbose_name='Quote Text'),
        ),
    ]
