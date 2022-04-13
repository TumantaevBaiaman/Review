from django.contrib import admin
from .models import (
    Post,
    Category,
    ReviewSchool,
    ReviewKindergarten,
    ReviewOffice
)

admin.site.register(Post)
admin.site.register(ReviewOffice)
admin.site.register(Category)
admin.site.register(ReviewSchool)
admin.site.register(ReviewKindergarten)


