# Generated by Django 2.1.5 on 2020-03-09 22:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='El el tiempo en que el objeto fue creado', verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, help_text='Es el tiempo en que el objeto se actualizo', verbose_name='Fecha de actualizacion')),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con este mismo correo'}, max_length=254, unique=True, verbose_name='email login')),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(message='Numero telefonico debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.', regex='(\\(\\+?\\d{2,3}\\)[\\*|\\s|\\-|\\.]?(([\\d][\\*|\\s|\\-|\\.]?){6})(([\\d][\\s|\\-|\\.]?){2})?|(\\+?[\\d][\\s|\\-|\\.]?){8}(([\\d][\\s|\\-|\\.]?){2}(([\\d][\\s|\\-|\\.]?){2})?)?)$')], verbose_name='Telefono')),
                ('mobile_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Numero celular debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.', regex='(\\(\\+?\\d{2,3}\\)[\\*|\\s|\\-|\\.]?(([\\d][\\*|\\s|\\-|\\.]?){6})(([\\d][\\s|\\-|\\.]?){2})?|(\\+?[\\d][\\s|\\-|\\.]?){8}(([\\d][\\s|\\-|\\.]?){2}(([\\d][\\s|\\-|\\.]?){2})?)?)$')], verbose_name='Celular')),
                ('ext', models.IntegerField(default=0, verbose_name='Extension telefono')),
                ('is_verified', models.BooleanField(default=False, help_text='Establece verdadero si el usuario tiene verficado su email', verbose_name='Verificacion')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='UserPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='El el tiempo en que el objeto fue creado', verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, help_text='Es el tiempo en que el objeto se actualizo', verbose_name='Fecha de actualizacion')),
                ('client', models.BooleanField(default=False, verbose_name='Cliente')),
                ('supervisor_pdo', models.BooleanField(default=False, verbose_name='Supervisor de programa de obra')),
                ('supervisor_ado', models.BooleanField(default=False, verbose_name='Supervisor de avances de obra')),
                ('employee', models.BooleanField(default=False, verbose_name='Empleado')),
                ('director', models.BooleanField(default=False, verbose_name='Director')),
                ('management', models.BooleanField(default=False, verbose_name='Administrador')),
            ],
            options={
                'ordering': ('employee',),
            },
        ),
        migrations.CreateModel(
            name='UserRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='El el tiempo en que el objeto fue creado', verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, help_text='Es el tiempo en que el objeto se actualizo', verbose_name='Fecha de actualizacion')),
                ('position', models.CharField(choices=[('GE Costos', 'Costos'), ('GE Contabilidad', 'Contabilidad'), ('GE Tramitologia', 'Tramitologia'), ('GE Estimaciones', 'Estimaciones'), ('GE Compras', 'Compras'), ('GE Avance de Obra', 'Avance de Obra'), ('GE Programa de obra', 'Programa de obra'), ('GE Residente', 'Residente'), ('Supervisor Avance de obra', 'Supervisor Avance de obra'), ('Supervisor Programa de obra', 'Supervisor Programa de obra'), ('Cliente', 'Cliente'), ('Director', 'Director'), ('Administrador', 'Administrador')], max_length=50, verbose_name='Cargo')),
                ('cost', models.BooleanField(default=False, verbose_name='Rol costos')),
                ('accounting', models.BooleanField(default=False, verbose_name='Rol contabilidad')),
                ('tramitology', models.BooleanField(default=False, verbose_name='Rol tramitologia')),
                ('estimation', models.BooleanField(default=False, verbose_name='Rol estimaciones')),
                ('shopping', models.BooleanField(default=False, verbose_name='Rol compras')),
                ('construction_advance', models.BooleanField(default=False, verbose_name='Rol avances de obras')),
                ('construction_program', models.BooleanField(default=False, verbose_name='Rol programa de obra')),
                ('resident', models.BooleanField(default=False, verbose_name='Rol Residente')),
            ],
            options={
                'ordering': ('-position',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='userPerson',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userPerson', to='users.UserPerson'),
        ),
        migrations.AddField(
            model_name='user',
            name='userRol',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userRol', to='users.UserRol'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
