from django.contrib import admin
from .models import Homepage, Login, NovaTurma, Cadastro, Lixeira, Processo, Funcionario, Usuario, In_progress_file, Finished_file

admin.site.register(Homepage)
admin.site.register(Login)
admin.site.register(NovaTurma)
admin.site.register(Cadastro)
admin.site.register(Lixeira)
admin.site.register(Processo)
admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(In_progress_file)
admin.site.register(Finished_file)