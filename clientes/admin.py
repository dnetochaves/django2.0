from django.contrib import admin
from .models import Person, Document

# Register your models here.
admin.site.register(Person)
admin.site.register(Document)