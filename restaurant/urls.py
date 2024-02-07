from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import MenuListCreateApi, MenuRetrieveUpdateDestroyApi
from .views import router

urlpatterns = [
    path('', views.index, name='index'),
    # authentication
    path('api-token-auth/', obtain_auth_token),

    # Menu urls
    path('menu-items', MenuListCreateApi.as_view(), name='menu_list_create'),
    path('menu-items/<int:pk>', MenuRetrieveUpdateDestroyApi.as_view(), name='menu_retrieve_update_destroy'),
    # Booking urls
    path('booking/', include(router.urls)),
]
