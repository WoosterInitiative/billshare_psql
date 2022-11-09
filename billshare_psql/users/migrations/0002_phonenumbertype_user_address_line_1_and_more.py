# Generated by Django 4.0.8 on 2022-11-07 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='type')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=50, verbose_name='line 1'),
        ),
        migrations.AddField(
            model_name='user',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=50, verbose_name='line 2'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='globals.state', verbose_name='state'),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15, verbose_name='ZIP code'),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US', verbose_name='phone number')),
                ('primary', models.BooleanField(default=False, verbose_name='primary contact number')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.phonenumbertype', verbose_name='type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='phonenumber',
            constraint=models.UniqueConstraint(condition=models.Q(('primary', 'True')), fields=('user',), name='only_one_primary_number'),
        ),
    ]
