from rest_framework import generics, filters

# Create your views here.
from .models import Category, Notes
from .serializer import CategorySerializer, NotesSerializer, AddNoteSerializer


class CreateCategoryAV(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'description'


class ListNotesAV(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["category__priority"]


class CreateNotesAV(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = AddNoteSerializer


class UpdateNotesAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
