from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdata = models.DateTimeField()
    # slug #TODO
    # id_publushed = models.BooleanField() #TODO
