from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from ERU3 import settings
from django.contrib.auth.views import login, logout_then_login
from django.views.static import serve

urlpatterns = [
        url(r'^$', views.IniciarSesion),
        url(r'^murogeneral/$', views.MuroGeneral),
        url(r'^perfil/$', views.Perfil),
        url(r'^registrarse/$', views.Registrarse),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
