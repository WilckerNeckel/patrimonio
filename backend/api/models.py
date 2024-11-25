from django.db import models


class Funcionario(models.Model):
    rfid_tag = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email_institucional = models.EmailField()
    cargo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

    
class Campus(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome
    
class Setor(models.Model):
    rfid_tag = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    bloco = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome
    
class Patrimonio(models.Model):
    rfid_tag = models.CharField(max_length=20, unique=True, null=True)

    descricao = models.CharField(max_length=100)
    data_aquisicao = models.DateField()
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.descricao

class Entrada(models.Model):
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    
class Saida(models.Model):
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    
class Alerta(models.Model):
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    
    
    