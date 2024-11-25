from rest_framework import viewsets
from .models import Patrimonio, Entrada, Saida, Alerta, Setor, Funcionario
from .serializers import SaidaSerializer, EntradaSerializer, AlertaSerializer, PatrimonioSerializer, SetorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class SaidaViewSet(viewsets.ModelViewSet):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class PatrimonioViewSet(viewsets.ViewSet):
    def list(self, request):
        rfidSetor = request.GET.get('rfidSetor')
        try:
            objectSetor = Setor.objects.get(rfid_tag=rfidSetor)  
            queryset = Patrimonio.objects.filter(setor=objectSetor)
        except Setor.DoesNotExist:
            return Response({"error": "Setor not found"}, status=404)
        
        serializer = PatrimonioSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    
class Registro(APIView):
    def post(self, request, *args, **kwargs):
        rfidFuncionario = request.data.get('rfidFuncionario')
        print(rfidFuncionario)
        rfidPatrimonio = request.data.get('rfidPatrimonio')
        print(rfidPatrimonio)
        rfidSetor = request.data.get('rfidSetor')
        print(rfidSetor)
        # Verifica se o Funcionario existe
        try:
            funcionario = Funcionario.objects.get(rfid_tag=rfidFuncionario)
        except Funcionario.DoesNotExist:
            return Response({'funcionario': False})

        # Obtém o Patrimonio
        patrimonio = get_object_or_404(Patrimonio, rfid_tag=rfidPatrimonio)
        setor_atual = patrimonio.setor

        # Verifica o setor e registra a movimentação
        if setor_atual.rfid_tag != rfidSetor:
            # Registra uma entrada no novo setor
            novo_setor = get_object_or_404(Setor, rfid_tag=rfidSetor)
            Entrada.objects.create(patrimonio=patrimonio, setor=novo_setor)
            patrimonio.setor = novo_setor
            patrimonio.save()
            return Response({'movimentacao': 'entrada', 'funcionario': True})
        else:
            # Registra uma saída para o setor de transporte (id 6)
            setor_transporte = get_object_or_404(Setor, id=6)
            Saida.objects.create(patrimonio=patrimonio, setor=setor_transporte)
            patrimonio.setor = setor_transporte
            patrimonio.save()
            return Response({'movimentacao': 'saida', 'funcionario': True})

    



# class RegistraEntrada(viewsets.ModelViewSet):
#     queryset = Entrada.objects.all()
#     serializer_class = EntradaSerializer
    
# class RegistraAlerta(viewsets.ModelViewSet):
#     queryset = Alerta.objects.all()
#     serializer_class = AlertaSerializer
    


