from rest_framework import viewsets
from rest_framework.decorators import action
from geenfy.models import Usuario, In_progress_file, Finished_file
from .serializers import UsuarioSerializer, In_progress_fileSerializer, Finished_fileSerializer
from django.http import FileResponse, Http404

class UsuarioReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class In_progress_fileViewSet(viewsets.ModelViewSet):
    queryset = In_progress_file.objects.all()
    serializer_class = In_progress_fileSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        try:
            documento = self.get_object()
            # Use o nome correto do campo aqui
            return FileResponse(documento.arquivo_inprogress.open(), as_attachment=True, filename=documento.arquivo_inprogress.name)
        except In_progress_file.DoesNotExist:
            raise Http404("Arquivo não encontrado")
        except AttributeError:
            raise Http404("Campo 'arquivo_inprogress' não encontrado no documento")
    
class Finished_FileViewSet(viewsets.ModelViewSet):
    queryset = Finished_file.objects.all()
    serializer_class = Finished_fileSerializer

