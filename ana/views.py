from django.conf import settings
from django.utils.module_loading import import_string
from django.views.generic import TemplateView

from rest_framework import viewsets, mixins

from .serializers import RecordSerializer
from .models import Record


APIAccessPermission = import_string(
    getattr(settings, 'ANA_API_ACCESS_PERMISSION',
            'ana.permissions.HasReadRecordsPermission')
)


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
    permission_classes = (APIAccessPermission,)


class DashboardView(TemplateView):
    template_name = 'ana/dashboard.html'
