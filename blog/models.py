from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:190]
 
    def pretty_pub_date(self):
        return self.pub_date.strftime(" %b %d %Y")