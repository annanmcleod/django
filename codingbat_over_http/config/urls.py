from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("near-hundred/<int:n>", near_hundred),
    path("string-splosion/<str:str>", string_splosion),
    path("cat-dog/<str:str>", cat_dog),
    path("lone-sum/<int:a>/<int:b>/<int:c>", lone_sum),
    path("admin/", admin.site.urls),
]
