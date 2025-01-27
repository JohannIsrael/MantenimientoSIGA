# Generated by Django 4.2.4 on 2024-05-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dep_mantenimiento', '0002_alter_historialsolicitud_nuevo_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialsolicitud',
            name='nuevo_status',
            field=models.CharField(choices=[('Enviado', 'Enviado'), ('Rechazado', 'Rechazado'), ('Solicitud_Firmada', 'Firmado'), ('Realizado', 'Realizado'), ('Pendiente', 'Pendiente'), ('En_espera', 'En espera'), ('En_proceso', 'En proceso')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitud_mantenimiento',
            name='folio',
            field=models.CharField(blank=True, default='Sin Sello', max_length=250),
        ),
        migrations.AlterField(
            model_name='solicitud_mantenimiento',
            name='status',
            field=models.CharField(blank=True, choices=[('Enviado', 'Enviado'), ('Rechazado', 'Rechazado'), ('Solicitud_Firmada', 'Firmado'), ('Realizado', 'Realizado'), ('Pendiente', 'Pendiente'), ('En_espera', 'En espera'), ('En_proceso', 'En proceso')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitud_mantenimiento',
            name='tipo_servicio',
            field=models.CharField(blank=True, choices=[('Cerrajería', 'Cerrajería'), ('Pintarrón', 'Pintarrón'), ('Cañones', 'Cañones'), ('Electrica', 'Electrica'), ('Herrería', 'Herrería'), ('Otro', 'Otro'), ('Plomería', 'Plomería'), ('Pintura', 'Pintura')], max_length=100),
        ),
        migrations.AlterField(
            model_name='trabajadores',
            name='puesto',
            field=models.CharField(blank=True, choices=[('Docente', 'Docente'), ('Secretario', 'Secretario/a'), ('Jefe', 'Jefe'), ('Subdirector', 'Subdirector/a'), ('Empleado', 'Empleado')], max_length=100, null=True),
        ),
    ]
