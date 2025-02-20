
from django.urls import path
from api import views
app_name = 'api'
urlpatterns = [
    path('clientes/', views.ClientesView.as_view(), name='clientes')
]
