from django.contrib import admin
from .models import Usuario, Administrador, Grupo, Subgrupo, SubgrupoGrupo, Integrante, IntegranteGrupo, IntegranteSubgrupo, Solicita, Tarefa, Avaliacao

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Grupo)
admin.site.register(Subgrupo)
admin.site.register(SubgrupoGrupo)
admin.site.register(Integrante)
admin.site.register(IntegranteGrupo)
admin.site.register(IntegranteSubgrupo)
admin.site.register(Solicita)
admin.site.register(Tarefa)
admin.site.register(Avaliacao)