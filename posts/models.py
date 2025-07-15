from django.db import models

class Post(models.Model):
    title  = models.CharField(max_length=254)
    content = models.CharField(max_length= 456)
    rate = models.IntegerField(default=0, null=True)
    create_at = models.CharField(max_length=254, default='To day')
    update_at = models.CharField(max_length=254, default='To day')

    def __str__(self):
        return f"{self.title} - {self.content}"