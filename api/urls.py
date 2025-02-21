
from django.urls import include, path
from api import views
from rest_framework.routers import SimpleRouter
from api import routers

app_name = 'api'
urlpatterns = [
    path('', include(routers.clienteAPIrouter.urls)),
    path('', include(routers.produtoAPIrouter.urls)),
    path('', include(routers.vendaAPIrouter.urls)),
]
