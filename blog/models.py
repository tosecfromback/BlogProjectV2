from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Post(models.Model):
    CATEGORY = (
        ('C-Lang' , 'C-Lang'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('HTML5', 'HTML5'),
        ('CSS', 'CSS'),
        ('Django', 'Django')

    )
    title = models.CharField(null=False, blank=False, max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=20, null=True, blank=True, choices=CATEGORY)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inheritance = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.content[:10]
