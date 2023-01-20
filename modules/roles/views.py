# Django 
from django.views.generic.base import TemplateView
# Utils
from modules.utils.mixins import AuthMixin

# tramitologia
class TramitologyView(AuthMixin, TemplateView):
    """ Tramitology panel """
    template_name = 'tramites/tramite_project.html'
    def get_context_data(self, **kwargs):
        context=super(TramitologyView, self).get_context_data(**kwargs)
        context['url'] = '/ge/roles/tramitologia/'
        return context

    
class TramitologyDataView(AuthMixin, TemplateView):
    template_name = 'tramites/tramite_project_data.html'

    def get_context_data(self, **kwargs):
        context=super(TramitologyDataView, self).get_context_data(**kwargs)
        nombre =  self.kwargs.get('name_project', None)
        pk = self.kwargs.get('pk', None)

        context['nombre'] = nombre
        context['pk'] = pk
        context['url'] = '/ge/roles/tramitologia/'

        return context
# costo

class CostoView(AuthMixin, TemplateView):
    """ Costo panel """
    template_name = 'costos/costo_project.html'


# contabilidad
class ContabilidadView(AuthMixin, TemplateView):
    """ panel project contabilidad """
    template_name = 'contabilidad/contabilidad_project.html'
    def get_context_data(self, **kwargs):
        context=super(ContabilidadView, self).get_context_data(**kwargs)
        context['url'] =  '/ge/roles/contabilidad/'
        return context


class ContabilidadDataView(AuthMixin, TemplateView):
    """data contabilidad """
    template_name = 'contabilidad/contablidad_project_data.html'
    def get_context_data(self, **kwargs):
        context=super(ContabilidadDataView, self).get_context_data(**kwargs)
        context['url'] =  '/ge/roles/contabilidad/'
        nombre =  self.kwargs.get('name_project', None)
        pk = self.kwargs.get('pk', None)

        context['nombre'] = nombre
        context['pk'] = pk
        return context


# estimaciones
class EstimacionesView(AuthMixin, TemplateView):
    """ pane project estimaciones """
    template_name = 'estimaciones/estimaciones_project.html'
    def get_context_data(self, **kwargs):
        context=super(EstimacionesView, self).get_context_data(**kwargs)
        context['url'] =  '/ge/roles/estimaciones/'
        return context


class EstimacionesDataView(AuthMixin, TemplateView):
    """ data estimaciones """
    template_name = 'estimaciones/estimaciones_project_data.html'
    def get_context_data(self, **kwargs):
        context=super(EstimacionesDataView, self).get_context_data(**kwargs)
        context['url'] =  '/ge/roles/estimaciones/'
        nombre =  self.kwargs.get('name_project', None)
        pk = self.kwargs.get('pk', None)
        context['nombre'] =  nombre
        context['pk'] = pk 
        return context

 # programa de obra    

class ProgramaDeObraView(AuthMixin, TemplateView):
    """panel de projectos dde programa de obra"""
    template_name =  'programa_de_obra/programa_de_obra_project.html'
    def get_context_data(self, **kwargs):
        context=super(ProgramaDeObraView, self).get_context_data(**kwargs)
        context['url'] = '/ge/roles/programaObra/'
        return context


class ProgramaDeObraDataView(AuthMixin, TemplateView):
    """ data programa de obra """
    template_name = 'programa_de_obra/programa_de_obra_project_data.html'
    def get_context_data(self, **kwargs):
        context=super(ProgramaDeObraDataView, self).get_context_data(**kwargs)
        context['url'] = '/ge/roles/programaObra/'
        nombre = self.kwargs.get('name_project', None)
        pk = self.kwargs.get('pk', None)
        context['nombre'] = nombre
        context['pk'] = pk
        return context
