# Cuidar para o que vai ser específico em cada página
# O que redenriza
# Qual a página que a gente vai renderizar
# Qual o conteúdo que essas páginas vão ter

'''
Primeiro passo: Criar uma view;
Segundo passo: Adicionar uma róta para essa view (urls);
'''

from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
