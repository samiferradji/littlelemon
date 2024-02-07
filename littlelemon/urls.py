from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser urls
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Restaurant app urls
    path('api/', include('restaurant.urls')),
    

]
