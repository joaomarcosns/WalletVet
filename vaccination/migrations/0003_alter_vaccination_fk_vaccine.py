# Generated by Django 4.0.5 on 2022-07-16 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0002_rename_pk_vaccine_vaccination_fk_vaccine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='fk_vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.vaccine'),
        ),
    ]
