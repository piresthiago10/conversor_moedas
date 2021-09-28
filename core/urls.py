from django.contrib import admin
from django.urls import path, include
from conversor_moedas.api.viewsets import ConversaoViewSet, ListaConversoes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('conversao', ConversaoViewSet, basename='Conversao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('listagem', ListaConversoes.as_view(), name="listagem")
]
