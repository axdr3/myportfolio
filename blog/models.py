from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=800)
    pub_date = models.DateTimeField()
