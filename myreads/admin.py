from django.contrib import admin
from .models import Gist, Comment

# Register your models here.
admin.site.register(Gist)
admin.site.register(Comment)
