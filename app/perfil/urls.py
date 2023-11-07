from django.urls import path, include
from . import views

app_name = 'perfil'


urlpatterns = [
    path('', views.CreatePerfilView.as_view(), name="create_perfil"),
    path('update/', views.UpdatePerfilView.as_view(), name="update_perfil"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
