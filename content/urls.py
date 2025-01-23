from django.urls import path
from .views import (
    ProjectListView, project_new)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", ProjectListView.as_view(), name="projects"),
    path("project_new", project_new, name = "project_new")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)