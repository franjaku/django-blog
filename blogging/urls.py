from django.urls import path
from blogging.views import detail_view, list_view, add_post_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/new/', add_post_view, name='new_post'),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]