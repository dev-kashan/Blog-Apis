from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.contrib.auth.models import User

# RATING = (
#     (1 , '1'),
#     (2 , '2'),
#     (3 , '3'),
#     (4 , '4'),
#     (5 , '5'),
# )



class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,default='',blank=True,null=True)
    image = models.ImageField(upload_to='app/images')
    
    class Meta:
        verbose_name_plural="01 Categories"

    def image_tag(self):
        return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Category , self).save(*args,**kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='app/images')
    detail = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="02 Blog"

    def image_tag(self):
        return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))

    def __str__(self):
        return self.title
