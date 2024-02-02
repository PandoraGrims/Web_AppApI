from django.urls import path

from webapp_api.views import view_add, view_subtract, view_multiply, view_divide, index

app_name = "webapp_api"

urlpatterns = [
    path("", index, name="index"),
    path("api_v1/add/", view_add, name="view_add"),
    path("api_v1/subtract/", view_subtract, name="view_subtract"),
    path("api_v1/multiply/", view_multiply, name="view_multiply"),
    path("api_v1/divide/", view_divide, name="view_divide"),
]