from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default=None, null=True, blank=True, upload_to="images/",
        editable=True,
        help_text="Header picture",
        verbose_name="Header picture")
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.date

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def __unicode__(self):
        return "{0}".format(self.image)

    def save(self):
        if not self.image:
            return            

        super(Post, self).save()
        image = Image.open(self.image)
        (width, height) = image.size     
        size = (1080, 400)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)