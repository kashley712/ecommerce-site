import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    #..
   # def __str__(self):
      #  return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelt(days=1)
        # Assuming you have imported the necessary models

# Retrieve the queryset
#questions = Question.objects.filter(question_text__startswith='Your query string')

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    #..
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)