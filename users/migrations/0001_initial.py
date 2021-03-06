# Generated by Django 4.0.5 on 2022-07-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('phone2', models.CharField(max_length=20, verbose_name='Phone 2')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('district', models.CharField(max_length=200, verbose_name='District')),
                ('street', models.CharField(max_length=250, verbose_name='street')),
                ('number', models.CharField(max_length=5, verbose_name='Number')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
