from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.default_view),
    path('pred/', include('pred.urls')),
]
