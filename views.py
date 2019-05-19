from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from blog.models import Blog_model, File_model, Comment_model


def blog_view(request):

    food_blog_list = Blog_model.objects.filter(type = "FOOD").order_by("-update_time")       # Decreasing order of Updated Time
    travel_blog_list = Blog_model.objects.filter(type = "TRAVEL").order_by("-update_time")       # Decreasing order of Updated Time
    photo_blog_list = Blog_model.objects.filter(type = "PHOTOGRAPHY").order_by("-update_time")       # Decreasing order of Updated Time

    return render(request, "blog/homepage.html",   {"food_blogs": food_blog_list,
                                                "travel_blogs": travel_blog_list,
                                                "photo_blogs": photo_blog_list,
                                                }
                  )

def open_blog(request, blog_id):
    # file_dict = {}
    # comment_dict = {}

    blog = Blog_model.objects.get(id = blog_id)
    file_list = File_model.objects.filter(blog_id = blog_id)
    comment_list = Comment_model.objects.filter(blog_id = blog_id)
    user_dict = {"blog": blog,
                 "files": file_list,
                 "comments": comment_list,
                 }
    return render(request, "blog/blog_detail.html", user_dict)

def create_blog(request):

    if request.method == "POST":
        b = Blog_model(type = request.POST['blog_type'].strip().upper(), title = request.POST['blog_title'].strip(), substance = request.POST['blog_substance'].strip(),
                       thumbnail = request.FILES["blog_thumb"], text = request.POST['blog_text'].strip())
        b.save()

        for i in request.FILES.getlist("media"):
            f = File_model(blog_id=b, file_name=i)
            f.save()

        # c = Comment_model(blog_id=b, text=request.POST['comment_text'])
        # c.save()
        return redirect("blog:blog_view")

    return render(request, "blog/new_blog.html")

def edit_blog(request, blog_id):

    blog_to_update = Blog_model.objects.get(id = blog_id)

    if request.method == "POST":
        blog_to_update.title = request.POST["new_title"]
        blog_to_update.text = request.POST["new_text"]
        blog_to_update.save()
        for i in request.FILES.getlist("media"):
            f = File_model(blog_id=blog_to_update, file_name=i)
            f.save()
        messages.success(request, "Blog Updation Successful")
        return redirect("blog:blog_view")

    # elif request.method == "GET":
    return render(request, "blog/edit.html", {"data":blog_to_update})


def delete_blog(request, blog_id):

    blog_to_delete = Blog_model.objects.get(id = blog_id)

    if request.method == "POST":
        if request.POST["response"].upper() == "DELETE":
            comments_to_delete =  Comment_model.objects.filter(blog_id = blog_id)
            files_to_delete =  File_model.objects.filter(blog_id = blog_id)

            # Deleting from Blog_model, Comment_model and File_model
            blog_to_delete.delete()
            comments_to_delete.delete()
            files_to_delete.delete()

        return redirect("blog:blog_view")

    # elif request.method == "GET":
    return render(request, "blog/delete.html", {"data":blog_to_delete})


def comment_blog(request, blog_id):

    blog_to_comment = Blog_model.objects.get(id = blog_id)

    if request.method == "POST":
        new_comment = request.POST["blog_comment"]
        new_comment_obj = Comment_model(blog_id = blog_to_comment, text = new_comment)
        new_comment_obj.save()
        blog_to_comment.save()

        return redirect("blog:blog_view")

    # elif request.method == "GET":
    return render(request, "blog/comment_blog.html", {"data":blog_to_comment})


def edit_comment(request, comment_id):

    comment_to_update = Comment_model.objects.get(id = comment_id)
    # import pdb;pdb.set_trace()

    if request.method == "POST":
        comment_to_update.text = request.POST["new_text"]
        comment_to_update.save()
        comment_to_update.blog_id.save()
        messages.success(request, "Comment Updation Successful")
        return redirect("blog:blog_view")

    # elif request.method == "GET":
    return render(request, "blog/edit.html", {"data":comment_to_update})

def all_blog_type(request, type):
    import pdb;pdb.set_trace()



# def delete_comment(request, blog_id):
#
#     blog_to_delete = Blog_model.objects.get(id = blog_id)
#
#     if request.method == "POST":
#         if request.POST["response"].upper() == "DELETE":
#             comments_to_delete =  Comment_model.objects.filter(blog_id = blog_id)
#             files_to_delete =  File_model.objects.filter(blog_id = blog_id)
#
#             # Deleting from Blog_model, Comment_model and File_model
#             blog_to_delete.delete()
#             comments_to_delete.delete()
#             files_to_delete.delete()
#
#         return redirect("blog:blog_view")
#
#     # elif request.method == "GET":
#     return render(request, "blog/delete.html", {"data":blog_to_delete}
