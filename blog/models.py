from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()


    # Function returns blog titles at top level of admin web page
    def __str__(self):
        return self.title
