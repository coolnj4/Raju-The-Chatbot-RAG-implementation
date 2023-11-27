from django.urls import path
from django.conf.urls import include
from .views import (api_register_view,  api_getToken)


urlpatterns = [
    path('api_register/', api_register_view),
    path('api_auth/', api_getToken),
]