from django.db import models

# Create your models here.
class List(models.Model):
    '''A list of activities that the user will be doing'''
    title=models.CharField(max_length=200)
    task=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
