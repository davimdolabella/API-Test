
from django.urls import include, path
from api import views
from rest_framework.routers import SimpleRouter
from api import routers

from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView


app_name = 'api'
urlpatterns = [
    path('', include(routers.clienteAPIrouter.urls)),
    path('', include(routers.produtoAPIrouter.urls)),
    path('', include(routers.vendaAPIrouter.urls)),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
