
from django.contrib import admin
from django.urls import path, include
from main.views import Api, View

api_patterns = [
    path('filter', Api.filter)
]

view_patterns = [
    path("", View.index),
    path('user/<int:pkid>', View.orders)
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_patterns)),
    path('', include(view_patterns))
]
