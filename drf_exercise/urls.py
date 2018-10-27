
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from housing.views import HouseDataViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'house-data', HouseDataViewSet)


schema_view = get_swagger_view(title='House Data API', url='/')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),
]
