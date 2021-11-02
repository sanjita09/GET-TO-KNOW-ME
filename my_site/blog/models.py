from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_address=models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Tag(models.Model):
    caption=models.CharField(max_length=20)
    
    def __str__(self):
        return self.caption

class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    image=models.ImageField(upload_to="posts",null=True)
    date=models.DateField(auto_now=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    slug=models.SlugField(unique=True,default='',blank=True,null=False,db_index=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name='posts',null=True)
    tags=models.ManyToManyField(Tag,related_name='post')
    

    def get_absolute_url(self):
    	return reverse('post-detail-page',args=[self.slug])

class Comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    
    def __str__(self):
        return f"{self.title}"

