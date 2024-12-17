from django.contrib import admin

from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = (
        "owner",
        "highlighted",
    )


# Register your models here.
admin.site.register(Snippet, SnippetAdmin)
