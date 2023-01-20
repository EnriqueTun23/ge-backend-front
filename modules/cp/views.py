# Api codigos postales
from django.shortcuts import render
# serializer
from .serializer import CodigosPostalesSerializer
# model
from .models import CodigoPostales
# Pagination
from .pagination import CustomPageNumberPagination
# Django
from django.db.models import Q
# Rest framework
from rest_framework.generics import ListAPIView


class ApiCPView(ListAPIView):
    serializer_class = CodigosPostalesSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = CodigoPostales.objects.all()
        cp = self.request.query_params.get('codigo_postal', None)
        if cp is not None:
            queryset = queryset.filter(codigo_postal=cp)
        return queryset