from django.contrib import admin

# Register your models here.
from data.models import *

admin.site.register(BuiltBy)
admin.site.register(Repositories)
