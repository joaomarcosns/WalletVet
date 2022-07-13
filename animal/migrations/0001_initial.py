# Generated by Django 4.0.5 on 2022-07-13 21:02

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
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=150, verbose_name='Color')),
            ],
            options={
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='TypeAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_animal', models.CharField(max_length=100, verbose_name='Type Animal')),
            ],
            options={
                'db_table': 'type_animal',
            },
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=200, verbose_name='Breed')),
                ('fk_type_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.typeanimal')),
            ],
            options={
                'db_table': 'breed',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, verbose_name='Gender')),
                ('description', models.TextField(max_length=999, verbose_name='Description')),
                ('photo', models.ImageField(upload_to='', verbose_name='photo')),
                ('hair_type', models.CharField(choices=[('S', 'Small'), ('M', 'Mid'), ('L', 'Large')], max_length=1, verbose_name='hair Type')),
                ('fk_breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.breed')),
                ('fk_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.color')),
                ('fk_type_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.typeanimal')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'animal',
            },
        ),
    ]