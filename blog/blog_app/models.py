from django.db import models
from django.core.validators import validate_email
from django.utils.text import slugify


# Create your models here.


class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    emailAddress = models.EmailField(
        max_length=254, validators=[validate_email])

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.caption}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField()
    excerpt = models.CharField(max_length=300, null=True)
    content = models.CharField(max_length=600)
    slug = models.SlugField(default='', null=True, blank=True, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='author')
    tag = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class CommentsModel(models.Model):
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField(max_length=254, validators=[validate_email])
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    # def __str__(self):
    #     return f'{self.userName} '

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
