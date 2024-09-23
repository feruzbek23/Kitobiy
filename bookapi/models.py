from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    STATUS = (
        (1, 'In Progress'),
        (2, 'Completed') ,    
    )

    STARS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    rate_stars = models.IntegerField(choices=STARS, validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='user_books')
    
    def __str__(self):
        return self.title
    

# User Model

