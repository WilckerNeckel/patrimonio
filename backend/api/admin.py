from django.contrib import admin

from .models import Funcionario, Campus, Setor, Patrimonio, Entrada, Saida, Alerta
from django.contrib import admin
from .models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('rfid_tag', 'nome', 'cargo')
    
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    
class PatrimonioAdmin(admin.ModelAdmin):
    list_display= ('rfid_tag', 'descricao', 'setor')
    
class SetorAdmin(admin.ModelAdmin):
    list_display= ('rfid_tag', 'nome', 'campus', 'supervisor')
    
class EntradaAdmin(admin.ModelAdmin):
    list_display= ('patrimonio', 'data', 'funcionario', 'setor')

class SaidaAdmin(admin.ModelAdmin):
    list_display= ('patrimonio', 'data', 'funcionario', 'setor')


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Patrimonio, PatrimonioAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Saida, SaidaAdmin)


