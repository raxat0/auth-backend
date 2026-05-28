from django.urls import path

from apps.auth_system.views import (
    RegisterView,
    LoginView,
)

from apps.business.views import ProductsView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('products/', ProductsView.as_view()),
]