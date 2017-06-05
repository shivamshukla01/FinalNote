from django.contrib import admin
from .models import Note,Subject,Branch, Contact

admin.site.register(Note)
admin.site.register(Subject)
admin.site.register(Branch)
admin.site.register(Contact)