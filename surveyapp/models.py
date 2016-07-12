from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question (models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("Publish Data" ,auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice (models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

