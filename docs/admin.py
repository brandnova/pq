from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category),
admin.site.register(Faculty),
admin.site.register(Department),
admin.site.register(Level),
admin.site.register(Semester),
admin.site.register(Item),

