# Generated by Django 4.2.4 on 2024-05-19 01:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Grupo',
                'db_table': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='trabajadores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField(blank=True, null=True)),
                ('nombres', models.CharField(blank=True, db_column='nombres', max_length=40, null=True, verbose_name='Nombre(s)')),
                ('appaterno', models.CharField(blank=True, db_column='appaterno', max_length=40, null=True, verbose_name='Apellido Paterno')),
                ('apmaterno', models.CharField(blank=True, db_column='apmaterno', max_length=40, null=True, verbose_name='Apellido Materno')),
                ('activo', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], db_column='activo', default='activo', max_length=15, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('H', 'Hombre'), ('M', 'Mujer')], db_column='sexo', max_length=1, null=True, verbose_name='Sexo')),
                ('puesto', models.CharField(blank=True, choices=[('Secretario', 'Secretario/a'), ('Jefe', 'Jefe'), ('Subdirector', 'Subdirector/a'), ('Docente', 'Docente'), ('Empleado', 'Empleado')], max_length=100, null=True)),
                ('departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('campus', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Correo')),
                ('foto_Perfil', models.ImageField(blank=True, null=True, upload_to='dep_mantenimiento/img/Foto_Perfil', verbose_name='Imagen de Perfil')),
                ('grupos', models.ManyToManyField(blank=True, related_name='trabajadores', to='dep_mantenimiento.customgroup')),
            ],
            options={
                'verbose_name': 'Perfil de trabajador',
                'db_table': 'trabajador',
                'permissions': [('view_mantenimiento_trabajador', 'Usuarios de Mantenimiento de Equipo pueden ver'), ('change_mantenimiento_trabajador', 'Usuarios de Mantenimiento de Equipo pueden editar'), ('view_all_trabajador', 'Usuarios Solcitantes pueden ver'), ('change_all_trabajador', 'Usuarios Solcitantes pueden editar'), ('add_all_trabajador', 'Usuarios Solcitantes pueden agregar'), ('delete_all_trabajador', 'Usuarios Solcitantes pueden borrar')],
            },
        ),
        migrations.CreateModel(
            name='Solicitud_Mantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField(blank=True)),
                ('area_solicitante', models.CharField(blank=True, max_length=150)),
                ('responsable_Area', models.CharField(blank=True, max_length=300)),
                ('tipo_servicio', models.CharField(blank=True, choices=[('Plomería', 'Plomería'), ('Pintarrón', 'Pintarrón'), ('Cerrajería', 'Cerrajería'), ('Electrica', 'Electrica'), ('Cañones', 'Cañones'), ('Otro', 'Otro'), ('Pintura', 'Pintura'), ('Herrería', 'Herrería')], max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=3000)),
                ('des_Serv_Realizado', models.CharField(blank=True, max_length=3000, null=True)),
                ('des_Serv_no_Realizado', models.CharField(blank=True, max_length=3000, null=True)),
                ('motv_rechazo', models.CharField(blank=True, max_length=3000, null=True)),
                ('des_Peticion_Mat', models.CharField(blank=True, max_length=3000, null=True)),
                ('Mat_Rechazo', models.CharField(blank=True, max_length=3000, null=True)),
                ('Mat_Resuelto', models.CharField(blank=True, max_length=3000, null=True)),
                ('status', models.CharField(blank=True, choices=[('En_proceso', 'En proceso'), ('Realizado', 'Realizado'), ('Pendiente', 'Pendiente'), ('Solicitud_Firmada', 'Firmado'), ('Enviado', 'Enviado'), ('Rechazado', 'Rechazado'), ('En_espera', 'En espera')], max_length=50)),
                ('fecha', models.DateField(blank=True)),
                ('hora', models.TimeField(blank=True)),
                ('material_asignado', models.CharField(blank=True, max_length=3000, null=True)),
                ('material_utilizado', models.CharField(blank=True, max_length=3000, null=True)),
                ('firma_Jefe_Departamento', models.BooleanField(blank=True, default=False)),
                ('firma_Empleado', models.BooleanField(blank=True, default=False)),
                ('firma_Jefe_VoBo', models.BooleanField(blank=True, default=False)),
                ('resolvio', models.BooleanField(blank=True, default=False)),
                ('firma_Jefe_Departamento_img', models.ImageField(blank=True, null=True, upload_to='dep_mantenimiento/img/Firmas/Jefe')),
                ('firma_Empleado_img', models.ImageField(blank=True, null=True, upload_to='dep_mantenimiento/img/Firmas/Jefe/Empleado')),
                ('firma_Jefe_VoBo_img', models.ImageField(blank=True, null=True, upload_to='dep_mantenimiento/img/Firmas/VoBo')),
                ('ocultar', models.BooleanField(blank=True, default=False, verbose_name='Ocultar_Solicitud')),
                ('id_Empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_empleado', to='dep_mantenimiento.trabajadores')),
                ('id_Jefe_Departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_jefe_departamento', to='dep_mantenimiento.trabajadores')),
                ('id_Jefe_Mantenimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_jefe_mantenimiento', to='dep_mantenimiento.trabajadores')),
                ('id_Subdirectora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_subdirectora', to='dep_mantenimiento.trabajadores')),
                ('id_Trabajador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_trabajador', to='dep_mantenimiento.trabajadores')),
            ],
            options={
                'verbose_name': 'Solicitud_de_mantenimiento',
                'db_table': 'solicitud_mantenimiento',
                'permissions': [('view_Solicitud_Solicitante', 'Solicitante ver'), ('change_Solicitud_Solicitante', 'Solicitante cambiar'), ('add_Solicitud_Solicitante', 'Solicitante agregar'), ('delete_Solicitud_Solicitante', 'Solicitante borrar'), ('view_Solicitud_jefeDep', 'jefeDep ver'), ('change_Solicitud_jefeDep', 'jefeDep cambiar'), ('add_Solicitud_jefeDep', 'jefeDep agregar'), ('delete_Solicitud_jefeDep', 'jefeDep borrar'), ('view_Solicitud_subdirector', 'subdirector ver'), ('change_Solicitud_subdirector', 'subdirector cambiar'), ('add_Solicitud_subdirector', 'subdirector agregar'), ('delete_Solicitud_subdirector', 'subdirector borrar'), ('view_Solicitud_jefe_Mantenimiento', 'jefMantenimiento ver'), ('change_Solicitud_jefe_Mantenimiento', 'jefMantenimiento cambiar'), ('view_Solicitud_empleado_Mantenimiento', 'empMantenimiento ver'), ('change_Solicitud_empleado_Mantenimiento', 'empMantenimiento cambiar')],
            },
        ),
        migrations.CreateModel(
            name='imagenesEvidencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidenciasIMG', models.ImageField(blank=True, null=True, upload_to='dep_mantenimiento/img/Evidencias')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud', to='dep_mantenimiento.solicitud_mantenimiento')),
            ],
            options={
                'verbose_name': 'Evidencias',
                'db_table': 'Evidencias',
            },
        ),
        migrations.CreateModel(
            name='HistorialSolicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firma_Jefe_Departamento', models.BooleanField(blank=True, default=False)),
                ('firma_Empleado', models.BooleanField(blank=True, default=False)),
                ('firma_Jefe_VoBo', models.BooleanField(blank=True, default=False)),
                ('resolvio', models.BooleanField(blank=True, default=False)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('nuevo_status', models.CharField(choices=[('En_proceso', 'En proceso'), ('Realizado', 'Realizado'), ('Pendiente', 'Pendiente'), ('Solicitud_Firmada', 'Firmado'), ('Enviado', 'Enviado'), ('Rechazado', 'Rechazado'), ('En_espera', 'En espera')], max_length=50)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='dep_mantenimiento.solicitud_mantenimiento')),
            ],
            options={
                'verbose_name': 'Historial de Solicitud',
                'db_table': 'historial_solicitud',
            },
        ),
    ]