from django.contrib import admin

from .models import User, Title, Category

admin.site.register(User)

admin.site.register(Category)

admin.site.register(Title)
