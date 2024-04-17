from django.db import models
# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    STATUS = (
        ('1', 'Started'),
        ('2', 'In Progress'),
        ('3', 'Completed') ,    
    )
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS)
    book_file = models.FileField(upload_to='media/')
    user = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='owner')
    
    def __str__(self):
        return self.title
    

# User Model

