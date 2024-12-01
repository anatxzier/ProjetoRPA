from rest_framework import viewsets
from rest_framework.decorators import action
from geenfy.models import In_progress_file, Finished_file, ErrorLog
from .serializers import In_progress_fileSerializer, Finished_fileSerializer, ErrorLogSerializer
from rest_framework import status
from rest_framework.response import Response


class In_progress_fileViewSet(viewsets.ModelViewSet):
    queryset = In_progress_file.objects.all()
    serializer_class = In_progress_fileSerializer

    @action(detail=True, methods=['delete'], url_path='delete-in-progress', url_name='delete_in_progress')
    def delete_in_progress(self, request, pk=None):
        try:
            # Filtrar o arquivo pelo ID e status "Em Progresso"
            file_in_progress = In_progress_file.objects.get(id=pk, status='Em Progresso')
            file_in_progress.delete()
            return Response({"message": "Arquivo em progresso excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except In_progress_file.DoesNotExist:
            return Response({"error": "Arquivo não encontrado ou não está em progresso."}, status=status.HTTP_404_NOT_FOUND)

class Finished_FileViewSet(viewsets.ModelViewSet):
    queryset = Finished_file.objects.all()
    serializer_class = Finished_fileSerializer

class ErrorLogViewSet(viewsets.ModelViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer
