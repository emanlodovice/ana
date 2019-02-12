from django.views.generic import TemplateView
from rest_framework import viewsets, mixins

from .serializers import RecordSerializer
from .models import Record


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class RecordViewset(CreateListRetrieveViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class DashboardView(TemplateView):
    template_name = 'ana/dashboard.html'
