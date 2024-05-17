# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LigacaoFornPeca(models.Model):
    id_peca_forn = models.OneToOneField('TbPeca', models.DO_NOTHING, db_column='Id_peca_forn', primary_key=True)  # Field name made lowercase. The composite primary key (Id_peca_forn, Id_fornecedor) found, that is not supported. The first column is selected.
    id_fornecedor = models.ForeignKey('TbFornecedor', models.DO_NOTHING, db_column='Id_fornecedor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligacao_forn_peca'
        unique_together = (('id_peca_forn', 'id_fornecedor'),)


class LigacaoFuncProj(models.Model):
    id_funcionario = models.OneToOneField('TbFuncionario', models.DO_NOTHING, db_column='Id_Funcionario', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Funcionario, Id_Project) found, that is not supported. The first column is selected.
    id_project = models.ForeignKey('TbProject', models.DO_NOTHING, db_column='Id_Project')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligacao_func_proj'
        unique_together = (('id_funcionario', 'id_project'),)


class LigacaoProjForn(models.Model):
    id_project = models.OneToOneField('TbProject', models.DO_NOTHING, db_column='Id_Project', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Project, Id_fornecedor) found, that is not supported. The first column is selected.
    id_fornecedor = models.ForeignKey('TbFornecedor', models.DO_NOTHING, db_column='Id_fornecedor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligacao_proj_forn'
        unique_together = (('id_project', 'id_fornecedor'),)


class LigacaoProjPeca(models.Model):
    id_project = models.OneToOneField('TbProject', models.DO_NOTHING, db_column='Id_Project', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Project, Id_peca) found, that is not supported. The first column is selected.
    id_peca = models.ForeignKey('TbPeca', models.DO_NOTHING, db_column='Id_peca')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ligacao_proj_peca'
        unique_together = (('id_project', 'id_peca'),)


class TbDepartamento(models.Model):
    id_departamento = models.AutoField(db_column='id_Departamento', primary_key=True)  # Field name made lowercase.
    depert_setor = models.CharField(db_column='Depert_Setor', max_length=45)  # Field name made lowercase.
    depart_num = models.CharField(db_column='Depart_Num', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_departamento'


class TbDeposito(models.Model):
    id_deposito = models.AutoField(primary_key=True)
    dep_endereco = models.CharField(db_column='Dep_endereco', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_deposito'


class TbFornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    fornc_nome = models.CharField(db_column='fornc_Nome', max_length=45)  # Field name made lowercase.
    fornc_endereco = models.CharField(db_column='fornc_Endereco', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_fornecedor'


class TbFuncionario(models.Model):
    id_funcionario = models.AutoField(db_column='id_Funcionario', primary_key=True)  # Field name made lowercase.
    func_nome = models.CharField(db_column='Func_Nome', max_length=45)  # Field name made lowercase.
    func_sobrenome = models.CharField(db_column='Func_sobrenome', max_length=45)  # Field name made lowercase.
    func_end = models.CharField(db_column='Func_end', max_length=45)  # Field name made lowercase.
    func_tel = models.CharField(db_column='Func_tel', max_length=12)  # Field name made lowercase.
    func_salario = models.DecimalField(db_column='Func_Salario', max_digits=7, decimal_places=2)  # Field name made lowercase.
    departamento = models.ForeignKey(TbDepartamento, models.DO_NOTHING, db_column='departamento_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_funcionario'


class TbPeca(models.Model):
    id_peca = models.AutoField(primary_key=True)
    peca_nome = models.CharField(db_column='Peca_nome', max_length=45)  # Field name made lowercase.
    peca_cor = models.CharField(db_column='Peca_cor', max_length=45)  # Field name made lowercase.
    peca_peso = models.CharField(db_column='Peca_peso', max_length=12)  # Field name made lowercase.
    id_deposito = models.ForeignKey(TbDeposito, models.DO_NOTHING, db_column='id_deposito')

    class Meta:
        managed = False
        db_table = 'tb_peca'


class TbProject(models.Model):
    id_project = models.AutoField(db_column='id_Project', primary_key=True)  # Field name made lowercase.
    nome_projeto = models.CharField(db_column='Nome_projeto', max_length=45)  # Field name made lowercase.
    proj_orcam = models.DecimalField(db_column='Proj_Orcam', max_digits=7, decimal_places=2)  # Field name made lowercase.
    proj_horas_trab = models.TimeField(db_column='Proj_horas_trab')  # Field name made lowercase.
    proj_tel = models.CharField(db_column='Proj_tel', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_project'
