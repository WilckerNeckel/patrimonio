
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from api.views import SaidaViewSet, EntradaViewSet, AlertaViewSet, PatrimonioViewSet, SetorViewSet, Registro

router = DefaultRouter()
router.register(r'saida', SaidaViewSet, basename='saida')
router.register(r'entrada', EntradaViewSet, basename='entrada')
router.register(r'alerta', AlertaViewSet, basename='alerta')
router.register(r'patrimonio', PatrimonioViewSet, basename='patrimonio')
router.register(r'setor', SetorViewSet, basename='setor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/registro/', Registro.as_view())
]
