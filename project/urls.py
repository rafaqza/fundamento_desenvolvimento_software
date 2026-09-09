from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),  # mantém a rota existente
    path('forum/', include('forum.urls')),
    path('', RedirectView.as_view(url='/forum/', permanent=False), name='home'),
]