from django.contrib import admin
from django.urls import path
from app.views import *

# Request ====== work =====> Response

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_world),
    # path("hello/<name>/", hello_views),
    # path("roll-die/<int:sides>/", roll_die_view),
    # path("random-between/<int:lo>/<int:hi>/", random_between_view),
]
