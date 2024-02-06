from django.urls import path, include
from . import views
from .views import MenuListCreateApi, MenuRetrieveUpdateDestroyApi
from .views import router

urlpatterns = [
    path('', views.index, name='index'),

    # Menu urls
    path('menu', MenuListCreateApi.as_view(), name='menu_list_create'),
    path('menu/<int:pk>', MenuRetrieveUpdateDestroyApi.as_view(), name='menu_retrieve_update_destroy'),
    # Booking urls
    path('booking/', include(router.urls)),
]
