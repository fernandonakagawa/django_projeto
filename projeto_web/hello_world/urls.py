from django.urls import path
from hello_world import views
from hello_world.models import LogMessage

from .views import SignUpView

mensagens_list_view = views.MensagensListView.as_view(
    queryset=LogMessage.objects.order_by("-log_data")[:5],
    context_object_name="message_list",
    template_name="hello_world/mensagens.html"
)
urlpatterns = [
    path("", views.home, name="home"),
    path("hello_world/<nome>", views.ola_campeao,
    name="ola_campeao"),
    path("ola/<nome>", views.ola, name="ola"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("mensagens/", mensagens_list_view, name="mensagens"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
