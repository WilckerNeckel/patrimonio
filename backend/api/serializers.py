from rest_framework import serializers
from .models import Patrimonio, Entrada, Saida, Alerta, Setor

class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = '__all__'
        
class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'
        
class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
        
class PatrimonioSerializer(serializers.ModelSerializer):
    setor = serializers.SerializerMethodField()
    class Meta:
        model = Patrimonio
        fields = 'rfid_tag', 'descricao', 'data_aquisicao', 'setor'
    
    def get_setor(self, obj):
        setor = Setor.objects.filter(id=obj.setor.id).values('nome')
        return setor[0]["nome"] if setor else None
        
class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'