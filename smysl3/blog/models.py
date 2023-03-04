from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdata = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)
    # id_publushed = models.BooleanField() #TODO


    def __str__(self):
        return f'{self.pk} - {self.title} - {self.pubdata}'