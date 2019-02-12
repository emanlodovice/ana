from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import RecordViewset, DashboardView

from rest_framework import routers


record_router = routers.SimpleRouter()
record_router.register('records', RecordViewset)


urlpatterns = [
    path('', DashboardView.as_view(), name='ana-dashboard'),
    url(r'^api/', include(record_router.urls)),
    url(r'^admin/', admin.site.urls),
]
