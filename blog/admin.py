from django.contrib import admin

from models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = ["published", "title", "slug", "content", "author", "category"]
    list_display = ["published", "title", "author", "created_at", "updated_at", "category"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated_at", "author", "category"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)

