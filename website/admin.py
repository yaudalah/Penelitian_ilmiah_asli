from django.contrib import admin
from .models import Post
from django.contrib.auth.models  import  Group

admin.site.register(Post)
admin.site.unregister(Group)

admin.site.site_header = "Admin Batik Pesisir"
admin.site.site_title = "Admin Batik Pesisir"
admin.site.index_title = "Batik Pesisir"
