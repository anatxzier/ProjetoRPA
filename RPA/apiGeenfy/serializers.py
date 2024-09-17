from rest_framework import serializers
from geenfy.models import Usuario, In_progress_file

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['user', 'login_IHX', 'senha_IHX', 'login_CAF', 'senha_CAF']

class In_progress_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_progress_file
        fields = ['id', 'arquivo_inprogress']
