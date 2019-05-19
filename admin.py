from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(Blog_model)
admin.site.register(File_model)
admin.site.register(Comment_model)
