from django.contrib import admin
from blogging.models import Post, Category


class PostInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )
    readonly_fields = ('posts', )
    # inlines = [
    #     PostInline,
    # ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
