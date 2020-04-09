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

    # readonly_fields = ('post_links', )
    #
    # def post_links(self):
    #     posts = Post.objects.all()
    #     list_return = ['<a href="/posts/{}"> {} </a>'.format(post.pk, post.title) for post in posts]
    #     return list_return


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
