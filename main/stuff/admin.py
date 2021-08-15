from django.contrib import admin
from .models import UserUpload

class UserUploadAdmin(admin.ModelAdmin):
    list_display = ('author', 'image', 'story', 'created', 'moderated')

admin.site.register(UserUpload, UserUploadAdmin)
