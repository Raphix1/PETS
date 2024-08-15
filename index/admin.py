from django.contrib import admin
from .models import Cats, Dogs, Hamsters
# Register your models here.

admin.site.register(Cats)
admin.site.register(Dogs)
admin.site.register(Hamsters)