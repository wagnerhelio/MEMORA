from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

# Autenticação e menu
from perform.views.login_views import login_ad_view, logout_view
from perform.views.menu_views import menu_view

# Clientes
from perform.views.cadastrar_clientes_views import cadastrar_clientes_view
from perform.views.listar_clientes_views import listar_clientes_view
from perform.views.editar_clientes_views import editar_clientes_view
from perform.views.excluir_clientes_views import excluir_clientes_view

# Faturamento
from perform.views.cadastrar_faturamento_view import cadastrar_faturamento_view 
from perform.views.listar_faturamento_view import listar_faturamento_view
from perform.views.editar_faturamento_view import editar_faturamento_view
from perform.views.excluir_faturamento_view import excluir_faturamento_view

# TipoFaturamento
from perform.views.cadastrar_tipo_faturamento_view import cadastrar_tipo_faturamento_view
from perform.views.listar_tipo_faturamento_view import listar_tipo_faturamento_view
from perform.views.editar_tipo_faturamento_view import editar_tipo_faturamento_view
from perform.views.excluir_tipo_faturamento_view import excluir_tipo_faturamento_view

# TipoIndicador
from perform.views.cadastrar_tipo_indicador_view import cadastrar_tipo_indicador_view
from perform.views.listar_tipo_indicador_view import listar_tipo_indicador_view
from perform.views.editar_tipo_indicador_view import editar_tipo_indicador_view
from perform.views.excluir_tipo_indicador_view import excluir_tipo_indicador_view


urlpatterns = [
    # Redirecionamento raiz para login
    path('', lambda request: redirect('login')),

    # Autenticação
    path('login/', login_ad_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Admin Django
    path('admin/', admin.site.urls),

    # Menu principal
    path('menu/', menu_view, name='menu'),

    # Clientes
    path('cadastrar/', cadastrar_clientes_view, name='cadastrar_clientes'),
    path('listar/', listar_clientes_view, name='listar_clientes'),
    path('editar/<int:cliente_id>/', editar_clientes_view, name='editar_clientes'),
    path('excluir/<int:cliente_id>/', excluir_clientes_view, name='excluir_clientes'),
    # Faturamento
    path('faturamento/cadastrar/', cadastrar_faturamento_view, name='cadastrar_faturamento'),
    path('faturamento/listar/', listar_faturamento_view, name='listar_faturamento'),
    path('faturamento/editar/<int:id>/', editar_faturamento_view, name='editar_faturamento'),
    path('faturamento/excluir/<int:id>/', excluir_faturamento_view, name='excluir_faturamento'),
    
    # TipoFaturamento
    path('tipo-faturamento/cadastrar/', cadastrar_tipo_faturamento_view, name='cadastrar_tipo_faturamento'),
    path('tipo-faturamento/listar/', listar_tipo_faturamento_view, name='listar_tipo_faturamento'),
    path('tipo-faturamento/editar/<int:id>/', editar_tipo_faturamento_view, name='editar_tipo_faturamento'),
    path('tipo-faturamento/excluir/<int:id>/', excluir_tipo_faturamento_view, name='excluir_tipo_faturamento'),

    # TipoIndicador
    path('tipo-indicador/cadastrar/', cadastrar_tipo_indicador_view, name='cadastrar_tipo_indicador'),
    path('tipo-indicador/listar/', listar_tipo_indicador_view, name='listar_tipo_indicador'),
    path('tipo-indicador/editar/<int:id>/', editar_tipo_indicador_view, name='editar_tipo_indicador'),
    path('tipo-indicador/excluir/<int:id>/', excluir_tipo_indicador_view, name='excluir_tipo_indicador'),
]
