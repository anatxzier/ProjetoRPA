from rest_framework import serializers # Importa o módulo serializers para criar serializers no Django REST Framework.
from geenfy.models import  In_progress_file, Finished_file, ErrorLog # Importa os modelos que serão serializados.

# Serializer para o modelo In_progress_file
class In_progress_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_progress_file
        fields = ['id', 'turma', 'arquivo_inprogress', 'status', 'upload_time'] # Campos que serão incluídos na serialização.

# Serializer para o modelo Finished_file
class Finished_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finished_file
        fields = ['id', 'turma', 'arquivo_fineshed', 'upload_time'] # Campos que serão incluídos na serialização.
        
# Serializer para o modelo ErrorLog        
class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = ['id', 'mensagem', 'data_criacao'] # Campos que serão incluídos na serialização.
