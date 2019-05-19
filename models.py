from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

def get_media_file_name(instance, filename):

    if instance.__class__.__name__.lower() == "blog_model":     # GIVES CLASS NAME OF instance. "type(instance).__name__" could also be used
        base_folder = "thumbnails"
        title = instance.title
        slug = slugify(title)
        return "%s/%s-%s" % (base_folder, slug, filename)

    else:
        base_folder = "blog"
        folder_name = instance.blog_id.id
        title = instance.blog_id.title
        slug = slugify(title)
        return "%s/%s/%s-%s" % (base_folder, folder_name, slug, filename)


class Blog_model(models.Model):
    # TYPE_CHOICE = [
    #                 ("FOOD", "Food"),
    #                 ("TRAVEL", "Travel"),
    #                 ("PHOTOGRAPHY", "Photography"),
    #               ]
    # type = models.CharField(max_length = 50, choices = TYPE_CHOICE, default = "FOOD")
    type = models.CharField(max_length = 50, default = "FOOD")
    count = models.PositiveIntegerField(default = 0)
    title = models.CharField(max_length = 500)
    substance = models.CharField(max_length = 5000, null = True)
    thumbnail = models.ImageField(upload_to = get_media_file_name, null = True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        # if not self.id:
        #     if Blog_model.objects.all():
        #         self.count = Blog_model.objects.order_by("id").last().count + 1
        #     else:
        #         self.count = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.title)

class File_model(models.Model):
    blog_id = models.ForeignKey(Blog_model, on_delete = models.CASCADE)
    file_name = models.FileField(upload_to = get_media_file_name)
    upload_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.file_name)

class Comment_model(models.Model):
    blog_id = models.ForeignKey(Blog_model, on_delete = models.CASCADE)
    # name = models.CharField(max_length = 30, null = False, blank = False, default = "Anonymous")
    # email = models.EmailField(max_length = 100, null = True, blank = False, default = "")
    text = models.CharField(max_length = 5000, blank = True, default = "")
    comment_time = models.DateTimeField(auto_now_add = True)
    comment_update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return (self.text)


