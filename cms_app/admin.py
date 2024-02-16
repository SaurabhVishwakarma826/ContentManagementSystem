from django.contrib import admin
from .models import CustomUser, Content, Category
# Register your models here.
admin.site.register(Content)
admin.site.register(CustomUser)
admin.site.register(Category)