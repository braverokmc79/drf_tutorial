from django.contrib import admin
from .models import Snippet


class SinippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos', 'language', 'style')
    list_filter = ('language', 'style')



admin.site.register(Snippet, SinippetAdmin)


