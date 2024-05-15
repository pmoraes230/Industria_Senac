from django.shortcuts import render
from .models import TbFuncionario

def cadastrar_funcionario(request):
    if request.method == 'POST':
        if request.POST.get('func_nome') and request.POST.get('func_sobrenome') and request.POST.get('func_end') and request.POST.get('func_tel') and request.POST.get('func_salario') and request.POST.get('departamento'):
            saverecord = TbFuncionario()
            saverecord.func_nome = request.POST.get('func_nome')
            saverecord.func_sobrenome = request.POST.get('func_sobrenome')
            saverecord.func_end = request.POST.get('func_end')
            saverecord.func_tel = request.POST.get('func_tel')
            saverecord.func_salario = request.POST.get('func_salario')
            saverecord.departamento = request.POST.get('departamento')
            saverecord.save()
            
            return render(request, 'login/login.html')
    else:
        return render(request, 'login/cadastrar_funcionario.html')

def login(request):
    return render(request, 'login/login.html')