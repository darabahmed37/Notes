from rest_framework import generics

# Create your views here.
from .models import Category, Notes
from .serializer import CategorySerializer, NotesSerializer


class CreateCategoryAV(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'description'


class CreateNotesAV(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class UpdateNotesAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
