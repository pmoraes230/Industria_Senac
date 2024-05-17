from django.shortcuts import render, redirect
from .models import TbFuncionario
from .models import TbDepartamento

def cadastrar_funcionario(request):
    departamentos = TbDepartamento.objects.all()  # Busque todos os departamentos
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['func_nome', 'func_sobrenome', 'func_end', 'func_tel', 'func_salario', 'departamento']):
            departamento_ID = request.POST.get('departamento')  # Obtém o ID do departamento do formulário

            # Verifica se o departamento existe
            departamento = TbDepartamento.objects.get(pk=departamento_ID)

            # Cria uma nova instância de TbFuncionario e associa o departamento
            saverecord = TbFuncionario()
            saverecord.func_nome = request.POST.get('func_nome')
            saverecord.func_sobrenome = request.POST.get('func_sobrenome')
            saverecord.func_end = request.POST.get('func_end')
            saverecord.func_tel = request.POST.get('func_tel')
            saverecord.func_salario = request.POST.get('func_salario')
            saverecord.departamento = departamento  # Associa o departamento ao funcionário

            saverecord.save()
            return render(request, 'login/cadastrar_funcionario.html', {'departamentos': departamentos})  # Passe os departamentos para o template
    return render(request, 'login/cadastrar_funcionario.html', {'departamentos': departamentos})  # Passe os departamentos para o template

def login(request):
    return render(request, 'login/login.html')