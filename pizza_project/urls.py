
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from pizza_auth_app import urls as pizza_auth_urls
from pizza_app import urls as pizza_urls
from pizza_app.views import index
from rest_api_app import urls as rest_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include(pizza_urls, namespace='pizza')),
    path('auth/', include(pizza_auth_urls, namespace='auth_app')),
    path('api/', include(rest_urls, namespace='rest_app')),
    path('', index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        path(r'__dubug__', include(debug_toolbar.urls)),
    ]