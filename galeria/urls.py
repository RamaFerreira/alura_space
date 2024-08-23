'''
Essa página não existia na configuração padrão
e foi criada para listar todas as urls das views criadas
e por fim mandar para url.py do setup
'''

from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name = ''),
    path('imagem/', imagem, name = 'imagem')
]
