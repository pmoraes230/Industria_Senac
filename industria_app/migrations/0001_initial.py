# Generated by Django 4.2.13 on 2024-05-15 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDepartamento',
            fields=[
                ('id_departamento', models.AutoField(db_column='id_Departamento', primary_key=True, serialize=False)),
                ('depert_setor', models.CharField(db_column='Depert_Setor', max_length=45)),
                ('depart_num', models.CharField(db_column='Depart_Num', max_length=12)),
            ],
            options={
                'db_table': 'tb_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDeposito',
            fields=[
                ('id_deposito', models.AutoField(primary_key=True, serialize=False)),
                ('dep_nome', models.CharField(db_column='dep_nome', max_length=45)),
                ('dep_endereco', models.CharField(db_column='Dep_endereco', max_length=50)),
            ],
            options={
                'db_table': 'tb_deposito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbFornecedor',
            fields=[
                ('id_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('fornc_nome', models.CharField(db_column='fornc_Nome', max_length=45)),
                ('fornc_endereco', models.CharField(db_column='fornc_Endereco', max_length=50)),
            ],
            options={
                'db_table': 'tb_fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbFuncionario',
            fields=[
                ('id_funcionario', models.AutoField(db_column='id_Funcionario', primary_key=True, serialize=False)),
                ('func_nome', models.CharField(db_column='Func_Nome', max_length=45)),
                ('func_sobrenome', models.CharField(db_column='Func_sobrenome', max_length=45)),
                ('func_end', models.CharField(db_column='Func_end', max_length=45)),
                ('func_tel', models.CharField(db_column='Func_tel', max_length=12)),
                ('func_salario', models.DecimalField(db_column='Func_Salario', decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'tb_funcionario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbPeca',
            fields=[
                ('id_peca', models.AutoField(primary_key=True, serialize=False)),
                ('peca_nome', models.CharField(db_column='Peca_nome', max_length=45)),
                ('peca_cor', models.CharField(db_column='Peca_cor', max_length=45)),
                ('peca_peso', models.CharField(db_column='Peca_peso', max_length=12)),
            ],
            options={
                'db_table': 'tb_peca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbProject',
            fields=[
                ('id_project', models.AutoField(db_column='id_Project', primary_key=True, serialize=False)),
                ('nome_projeto', models.CharField(db_column='Nome_projeto', max_length=45)),
                ('proj_orcam', models.DecimalField(db_column='Proj_Orcam', decimal_places=2, max_digits=7)),
                ('proj_horas_trab', models.TimeField(db_column='Proj_horas_trab')),
                ('proj_tel', models.CharField(db_column='Proj_tel', max_length=12)),
            ],
            options={
                'db_table': 'tb_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LigacaoFornPeca',
            fields=[
                ('id_peca_forn', models.OneToOneField(db_column='Id_peca_forn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='industria_app.tbpeca')),
            ],
            options={
                'db_table': 'ligacao_forn_peca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LigacaoFuncProj',
            fields=[
                ('id_funcionario', models.OneToOneField(db_column='Id_Funcionario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='industria_app.tbfuncionario')),
            ],
            options={
                'db_table': 'ligacao_func_proj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LigacaoProjForn',
            fields=[
                ('id_project', models.OneToOneField(db_column='Id_Project', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='industria_app.tbproject')),
            ],
            options={
                'db_table': 'ligacao_proj_forn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LigacaoProjPeca',
            fields=[
                ('id_project', models.OneToOneField(db_column='Id_Project', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='industria_app.tbproject')),
            ],
            options={
                'db_table': 'ligacao_proj_peca',
                'managed': False,
            },
        ),
    ]
