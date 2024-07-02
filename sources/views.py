# sources/views.py
from .forms import TarefaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Administrador, Grupo, Subgrupo, Tarefa, Avaliacao
from django.http import HttpResponse

# Views existentes
def index(request):
    grupo1 = {
        'groups_data': [
            {'nome': 'Marcos', 'integrantes': 5, 'tarefas': 10, 'representante': {'nome': 'Rosa'},
            'integrantes': [
                {'nome': 'Rosa'}
            ]},
            {'nome': 'Felipe', 'integrantes': 3, 'tarefas': 8},
            {'nome': 'Jessica', 'integrantes': 7, 'tarefas': 15},
        ],

        'integrantes': [
            {'nome': 'João', 'tem_subgrupo': True},
            {'nome': 'Maria', 'tem_subgrupo': False},
            {'nome': 'Pedro', 'tem_subgrupo': True},
            {'nome': 'João', 'tem_subgrupo': False},
            {'nome': 'Maria', 'tem_subgrupo': False},
            {'nome': 'Pedro', 'tem_subgrupo': False},
            {'nome': 'João', 'tem_subgrupo': False},
            {'nome': 'Maria', 'tem_subgrupo': False},
            {'nome': 'Pedro', 'tem_subgrupo': True},
        ],

        'tarefas': [
            {'descricao': 'Fazer uma aplicação mobile', 'data_entrega': '01/07/2024'}
        ]
    }

    grupo2 = {
        'groups_data': [
            {'nome': 'Ana', 'integrantes': 6, 'tarefas': 12, 'representante': {'nome': 'Carlos'},
            'integrantes': [
                {'nome': 'Carlos'}
            ]},
            {'nome': 'Lucas', 'integrantes': 4, 'tarefas': 7},
            {'nome': 'Sofia', 'integrantes': 8, 'tarefas': 20},
        ],

        'integrantes': [
            {'nome': 'Paulo', 'tem_subgrupo': True},
            {'nome': 'Camila', 'tem_subgrupo': False},
            {'nome': 'Ricardo', 'tem_subgrupo': True},
            {'nome': 'Julia', 'tem_subgrupo': False},
            {'nome': 'Fernanda', 'tem_subgrupo': False},
            {'nome': 'Mateus', 'tem_subgrupo': False},
            {'nome': 'Andre', 'tem_subgrupo': False},
            {'nome': 'Mariana', 'tem_subgrupo': False},
            {'nome': 'Beatriz', 'tem_subgrupo': True},
        ],

        'tarefas': [
            {'descricao': 'Desenvolver um site', 'data_entrega': '10/07/2024'}
        ]
    }

    subgrupo = {'nome': 'Marcos', 'integrantes': 5, 'tarefas': 10, 'representante': {'nome': 'Rosa'},
            'integrantes': [
                {'nome': 'Marcos'}
            ]}

    view_param = request.GET.get('view', None)
    selected_group = request.GET.get('group', 'grupo1')

    grupo = grupo1 if selected_group == 'grupo1' else grupo2

    return render(request, 'index.html', {
        'view': view_param,
        'grupo': grupo,
        'subgrupo': subgrupo,
        'selected_group': selected_group
    })


def dashboard(request):
    view_param = request.GET.get('view', None)
    return render(request, 'index.html', {'view': view_param})


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            descricao = form.cleaned_data['descricao']
            data_entrega = form.cleaned_data['data_entrega']
            # Salvar os dados no banco de dados ou em outro sistema de armazenamento
            # Redirecionar para a página de visualização de todas as tarefas ou outra página de destino
            return redirect('todas_tarefas')
    else:
        form = TarefaForm()
    
    return render(request, 'console/criar_tarefa.html', {'form': form})

def submit_group(request):
    if request.method == 'POST':
        groupName = request.POST.get('groupName')
        numSubgroups = request.POST.get('numSubgroups')
        maxLimit = request.POST.get('maxLimit')

        return HttpResponse('Grupo criado com sucesso!')
    else:
        return HttpResponse('Método não permitido!')

def create_group(request):
    return render(request, 'create_group.html')


def integrante(request):
    return render(request, 'pages/integrante.html')

def administrador(request):
    return render(request, 'pages/administrador.html')

# Views para Usuario
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pages/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/usuario_form.html')

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/usuario_form.html', {'usuario': usuario})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'pages/usuario_confirm_delete.html', {'usuario': usuario})

# Views para Administrador
def administrador_list(request):
    administradores = Administrador.objects.all()
    return render(request, 'pages/administrador_list.html', {'administradores': administradores})

def administrador_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/administrador_form.html')

def administrador_update(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/administrador_form.html', {'administrador': administrador})

def administrador_delete(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        administrador.delete()
        return redirect('administrador_list')
    return render(request, 'pages/administrador_confirm_delete.html', {'administrador': administrador})

# Similar views for Grupo, Subgrupo, Tarefa, Avaliacao

# Views para Grupo
def grupo_list(request):
    grupo = Grupo.objects.all()
    return render(request, 'pages/grupo_list.html', {'grupos': grupo})

def grupo_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/grupo_form.html')

def grupo_update(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/grupo_form.html', {'grupos': grupo})

def grupo_delete(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        grupo.delete()
        return redirect('grupo_list')
    return render(request, 'pages/grupo_confirm_delete.html', {'grupos': grupo})


# Views para Subgrupo
def subgrupo_list(request):
    subgrupo = Subgrupo.objects.all()
    return render(request, 'pages/subgrupo_list.html', {'subgrupos': subgrupo})

def subgrupo_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/subgrupo_form.html')

def subgrupo_update(request, pk):
    subgrupo = get_object_or_404(Subgrupo, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/subgrupo_form.html', {'subgrupos': subgrupo})

def subgrupo_delete(request, pk):
    subgrupo = get_object_or_404(Subgrupo, pk=pk)
    if request.method == 'POST':
        subgrupo.delete()
        return redirect('subgrupo_list')
    return render(request, 'pages/subgrupo_confirm_delete.html', {'subgrupos': subgrupo})


# Views para Tarefa
def tarefa_list(request):
    tarefa = Tarefa.objects.all()
    return render(request, 'pages/tarefa_list.html', {'tarefas': tarefa})

def tarefa_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/tarefa_form.html')

def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/tarefa_form.html', {'grupos': tarefa})

def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_list')
    return render(request, 'pages/tarefa_confirm_delete.html', {'grupos': tarefa})


# Views para Avaliacao
def avaliacao_list(request):
    avaliacao = Avaliacao.objects.all()
    return render(request, 'pages/avaliacao_list.html', {'Avaliações': avaliacao})

def avaliacao_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/avaliacao_form.html')

def avaliacao_update(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'pages/avaliacao_form.html', {'Avaliações': avaliacao})

def avaliacao_delete(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        avaliacao_list.delete()
        return redirect('avaliacao_list')
    return render(request, 'pages/avaliacao_confirm_delete.html', {'Avaliações': avaliacao})