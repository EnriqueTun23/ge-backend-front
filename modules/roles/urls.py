# Django 
from django.urls import path, include
# Views Roles
from .views import (TramitologyView, TramitologyDataView, 
CostoView,
ContabilidadView, ContabilidadDataView,
EstimacionesView, EstimacionesDataView,
ProgramaDeObraView, ProgramaDeObraDataView)

urlpatterns = [
    # tramitologia
    path('tramitologia/', TramitologyView.as_view(), name='tramitologia'),
    path('tramitologia/<str:name_project>/<int:pk>/', TramitologyDataView.as_view(), name='tramitologiaList' ),
    # costo
    path('costos/', CostoView.as_view(), name='costo'),
    # contabilidad
    path('contabilidad/', ContabilidadView.as_view(), name='contabilidad'),
    path('contabilidad/<str:name_project>/<int:pk>/', ContabilidadDataView.as_view(), name='contabilidaData'),
    # estimaciones
    path('estimaciones/', EstimacionesView.as_view(), name='estimaciones'),
    path('estimaciones/<str:name_project>/<int:pk>/', EstimacionesDataView.as_view(), name='estimacionesData'),
    # programa de obra 
    path('programaObra/', ProgramaDeObraView.as_view(), name='programa_de_obra'),
    path('programaObra/<str:name_project>/<int:pk>/', ProgramaDeObraDataView.as_view(), name='programa_de_obraData'),

]