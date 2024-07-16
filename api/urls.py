from django.urls import path, include
from rest_framework import routers
from api import views

# urls/endpoints - basicamente esto es el router

router = routers.DefaultRouter()
router.register(r'articulos', views.ArticuloViewSet)  # la R es importante, evita que algunos caracteres se interpreten correctamente

urlpatterns=[
    path('',include(router.urls))
]
