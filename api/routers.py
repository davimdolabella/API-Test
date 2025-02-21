from rest_framework.routers import SimpleRouter
from api import views

clienteAPIrouter = SimpleRouter()
clienteAPIrouter.register(
    'cliente',
    views.ClienteViewSet,
    basename='cliente-api'
)

produtoAPIrouter = SimpleRouter()
produtoAPIrouter.register(
    'produto',
    views.ProdutoViewSet,
    basename='produto-api'
)

vendaAPIrouter = SimpleRouter()
vendaAPIrouter.register(
    'venda',
    views.VendaViewSet,
    basename='venda-api'
)