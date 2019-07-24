from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
# Create your views here.
from initialapp.models import *
from initialapp.serializers import *

#views -- holds business logic

class LibrarianVset(ReadOnlyModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSer


class LibraryVset(ReadOnlyModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySer

class BookVset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSer

class StudentVset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer



