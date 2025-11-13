from django.urls import path
from . import views

urlpatterns = [
    path("manual/", views.manual_cache_view, name="manual_cache"),
    path("view/", views.view_cache_view, name="view_cache"),
    path("query/", views.query_cache_view, name="query_cache"),
    path("template/", views.template_cache_view, name="template_cache"),
        path("tasks/", views.trigger_tasks, name="trigger_tasks"),
]
