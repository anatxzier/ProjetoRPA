import subprocess
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RodarScriptAPIView(APIView):
    def get(self, request, format=None):
        try:
            # Defina o caminho absoluto para o script
            script_path = r"C:\Users\Aluno\Documents\Test_tcc\test_terminal.py"

            # Verifique se o arquivo existe
            if not os.path.isfile(script_path):
                return Response({'status': 'erro', 'message': f'Arquivo não encontrado: {script_path}'}, status=status.HTTP_404_NOT_FOUND)

            # Executa o script usando o Python
            result = subprocess.run(["python", script_path], capture_output=True, text=True)

            # Retorna a saída do script
            if result.returncode == 0:
                return Response({'status': 'sucesso', 'output': result.stdout}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'erro', 'output': result.stderr}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'status': 'erro', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
