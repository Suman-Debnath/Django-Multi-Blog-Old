from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_view, name = "blog_view"),
    path("new", views.create_blog, name = "new_blog"),
    path("<int:blog_id>/edit_blog/", views.edit_blog, name = "edit_blog"),
    path("<int:blog_id>/comment/", views.comment_blog, name = "comment_blog"),
    path("<int:blog_id>/delete_blog/", views.delete_blog, name = "delete_blog"),
    path("<int:blog_id>/detail_blog/", views.open_blog, name = "open_blog"),
    path("<int:comment_id>/edit_comment/", views.edit_comment, name = "edit_comment"),
    # path("<int:comment_id>/delete_comment/", views.delete_comment, name = "delete_blog"),
]
