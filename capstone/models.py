from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    user = models.CharField(max_length=25)

    def __str__(self):
        return self.question
