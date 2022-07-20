from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateCategoryAV, UpdateCategoryAV, CreateNotesAV, UpdateNotesAV

urlpatterns = [
    path("cat/", CreateCategoryAV.as_view()),
    path("cat/<str:description>", UpdateCategoryAV.as_view()),
    path("notes/", CreateNotesAV.as_view()),
    path("notes/<int:pk>", UpdateNotesAV.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
