from django.db import models


class Blog(models.Model):
    url = models.CharField(max_length=200)
    date = models.DateField('Date')
    text = models.TextField()

    def __str__(self):
        return self.url