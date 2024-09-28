from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self) -> str:
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return self.date

class Users(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    emailadd = models.CharField(max_length=264)

""" top = Topic('asdf')
print(top) """