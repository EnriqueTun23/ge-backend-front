# Django rest framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 200

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))