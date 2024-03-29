# Generated by Django 3.2.3 on 2021-05-28 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_from', models.CharField(max_length=20, verbose_name='From')),
                ('age_to', models.CharField(max_length=20, verbose_name='To')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'Age Band',
                'verbose_name_plural': 'Age Bands',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.CharField(blank=True, max_length=20, null=True, verbose_name='Premium')),
                ('cover', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cover')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('age_band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.ageband')),
            ],
            options={
                'verbose_name': 'Policy',
                'verbose_name_plural': 'Policy',
            },
        ),
        migrations.CreateModel(
            name='PolicyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'Policy Type',
                'verbose_name_plural': 'Policy Types',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=20, null=True, verbose_name='Premium')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ACTIVE', 'ACTIVE'), ('ACCEPTED', 'ACCEPTED')], max_length=20, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='policy.policy')),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
        migrations.AddField(
            model_name='policy',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.policytype'),
        ),
    ]
