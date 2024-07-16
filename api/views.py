from rest_framework import viewsets
from .serializer import ArticuloSerializer
from .models import Articulo

# Create your views here.


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
