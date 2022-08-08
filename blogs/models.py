from django.db import models
from django.contrib.auth.models import User 

class BlogPost(models.Model):
    """A topic the user is learning about."""
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
