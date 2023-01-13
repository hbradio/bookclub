from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Discussion, Thread, Post

admin.site.register(User, UserAdmin)
admin.site.register(Discussion)
admin.site.register(Thread)
admin.site.register(Post)
