from django.contrib import admin
from .models import Album, Images, FileUpload


admin.site.register(Album)
admin.site.register(Images)
admin.site.register(FileUpload)

