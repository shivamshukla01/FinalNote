from django.contrib import admin
from .models import Note,Subject,Branch, Contact ,Paper

admin.site.register(Note)
admin.site.register(Subject)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Paper)