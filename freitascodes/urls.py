from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from freitascodes.views import CertificadosApiView, ProjetosApiView

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = DefaultRouter(trailing_slash=False)
router.register(r'api/certificados',CertificadosApiView, basename='CertificadosApiView')
router.register(r'api/projetos',ProjetosApiView, basename='ProjetosApiView')

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)