# Generated by Django 3.1.5 on 2021-01-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210119_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='estatus_de_inscripcion',
            field=models.BooleanField(default=False),
        ),
    ]