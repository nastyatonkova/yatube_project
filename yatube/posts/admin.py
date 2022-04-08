from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Fields that will be displayed by admin
    list_display = ('pk', 'text', 'pub_date', 'author')
    # Search interface for posts
    search_fields = ('text',)
    # Date filter
    list_filter = ('pub_date',)
    # Empty field
    empty_value_display = '-empty-'


# Configuration to register Post model as class PostAdmin
admin.site.register(Post, PostAdmin)
