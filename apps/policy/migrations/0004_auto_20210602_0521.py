# Generated by Django 3.2.3 on 2021-06-02 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('policy', '0003_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='policy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='policy.policy'),
            preserve_default=False,
        ),
    ]