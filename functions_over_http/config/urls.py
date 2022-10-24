from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("hey/<name>", hey_views),
    path("age-in/<int:end>/<int:birthyear>", how_old),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", take_order),
    path("admin/", admin.site.urls),
]
