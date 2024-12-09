from rest_framework import viewsets  # Importa viewsets para criar APIs baseadas em modelos.
from rest_framework.decorators import action # Permite adicionar ações personalizadas às views.
from geenfy.models import In_progress_file, Finished_file, ErrorLog # Importa os modelos utilizados.
from .serializers import In_progress_fileSerializer, Finished_fileSerializer, ErrorLogSerializer # Importa os serializers que definem como os dados serão serializados/desserializados.
from rest_framework import status # Importa códigos de status HTTP.
from rest_framework.response import Response # Fornece respostas personalizadas para as requisições.

# ViewSet para gerenciar objetos In_progress_file
class In_progress_fileViewSet(viewsets.ModelViewSet):
    queryset = In_progress_file.objects.all()
    serializer_class = In_progress_fileSerializer
    
    # Ação personalizada para deletar arquivos "em progresso"
    @action(detail=True, methods=['delete'], url_path='delete-in-progress', url_name='delete_in_progress')
    def delete_in_progress(self, request, pk=None):
        try:
            # Filtrar o arquivo pelo ID e status "Em Progresso"
            file_in_progress = In_progress_file.objects.get(id=pk, status='Em Progresso')
            file_in_progress.delete() # Exclui o arquivo encontrado.
            return Response({"message": "Arquivo em progresso excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT) # Retorna resposta de sucesso.
        except In_progress_file.DoesNotExist:
            return Response({"error": "Arquivo não encontrado ou não está em progresso."}, status=status.HTTP_404_NOT_FOUND) # Retorna erro caso o arquivo não seja encontrado ou o status não seja "Em Progresso".

# ViewSet para gerenciar objetos Finished_file
class Finished_FileViewSet(viewsets.ModelViewSet):
    queryset = Finished_file.objects.all()
    serializer_class = Finished_fileSerializer

# ViewSet para gerenciar objetos ErrorLog
class ErrorLogViewSet(viewsets.ModelViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer
