from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=70)
    decription=models.TextField()

    def __str__(self):
        return self.title