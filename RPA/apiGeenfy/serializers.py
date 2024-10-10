from rest_framework import serializers
from geenfy.models import  In_progress_file, Finished_file

class In_progress_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_progress_file
        fields = ['id', 'turma', 'arquivo_inprogress', 'status', 'upload_time']

class Finished_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finished_file
        fields = ['id', 'turma', 'arquivo_finished', 'upload_time']