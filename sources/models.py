from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Administrador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Admin: {self.user.nome}'

class Grupo(models.Model):
    admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    limit_subgrupo_membro = models.IntegerField()
    limit_subgrupo = models.IntegerField()
    convite_link = models.URLField()

    def __str__(self):
        return self.nome

class Subgrupo(models.Model):
    representante = models.ForeignKey('Integrante', on_delete=models.SET_NULL, null=True)
    grupo = models.ManyToManyField(Grupo, through='SubgrupoGrupo')

    def __str__(self):
        return f'Subgrupo {self.id}'

class SubgrupoGrupo(models.Model):
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Integrante(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=255)

    def __str__(self):
        return self.user.nome

class IntegranteGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)

class IntegranteSubgrupo(models.Model):
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)

class Solicita(models.Model):
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class Tarefa(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'Tarefa {self.id}'

class Avaliacao(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    entrega = models.DateField()
    participacao = models.TextField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    arquivo = models.FileField(upload_to='avaliacoes/')

    def __str__(self):
        return f'Avaliacao {self.id} - Tarefa {self.tarefa.id}'
