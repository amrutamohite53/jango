from django.contrib import admin

# Register your models here.
from initialapp.models import *

admin.site.register(Student)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)
