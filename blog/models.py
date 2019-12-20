from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=20)
    text = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.text[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
