from rest_framework import serializers

from .models import Category, Notes


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Notes
        fields = '__all__'


class AddNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
