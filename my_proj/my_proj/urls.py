from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from cac.admin import mi_admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cacadmin/', mi_admin.urls),
    path('', include('cac.urls'))
]
