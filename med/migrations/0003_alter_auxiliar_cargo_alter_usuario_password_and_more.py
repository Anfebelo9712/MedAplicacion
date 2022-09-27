# Generated by Django 4.1.1 on 2022-09-27 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_usuario_rol_alter_usuario_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliar',
            name='cargo',
            field=models.CharField(max_length=80, verbose_name='Profesion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('MEDICO', 'Med'), ('ENFERMER@', 'Enf'), ('PACIENTE', 'Pac'), ('FAMILIAR', 'Fam'), ('AUXILIAR', 'Aux')], default='PACIENTE', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Username'),
        ),
    ]
