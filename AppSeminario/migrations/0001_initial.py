# Generated by Django 4.1.3 on 2022-12-19 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=15)),
                ('fechainscripción', models.DateField()),
                ('horainscripción', models.TimeField()),
                ('estado', models.CharField(choices=[['Reservado', 'Reservado'], ['Completada', 'Completada'], ['Anulada', 'Anulada'], ['No Asisten', 'No Asisten']], max_length=30)),
                ('observacion', models.CharField(blank=True, max_length=200)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppSeminario.institucion')),
            ],
        ),
    ]
