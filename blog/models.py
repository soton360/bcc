from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title