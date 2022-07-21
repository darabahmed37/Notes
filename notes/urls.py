from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateCategoryAV, UpdateCategoryAV, ListNotesAV, UpdateNotesAV, CreateNotesAV

urlpatterns = [
    path("cat/", CreateCategoryAV.as_view()),
    path("cat/<str:description>", UpdateCategoryAV.as_view()),
    path("notes/", ListNotesAV.as_view()),
    path("notes/new/", CreateNotesAV.as_view()),
    path("notes/<int:pk>/", UpdateNotesAV.as_view()),
]