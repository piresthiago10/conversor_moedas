from django.contrib import admin
from django.urls import path, include
from conversor_moedas.api.viewsets import ConversaoViewSet, ListaConversoesViewSet, ListaConversoes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('conversao', ConversaoViewSet, basename='Conversao')
router.register('lista', ListaConversoesViewSet, basename='lista')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('from/<str:moeda_origem>/to/<str:moeda_final>/amount/<int:valor_conversao>', ListaConversoesViewSet, name="conversor"),
    path('listagem', ListaConversoes.as_view(), name="listagem")
]
