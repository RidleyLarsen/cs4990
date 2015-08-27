from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField()

    def __unicode__(self, *args, **kwargs):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=128)
    votes = models.PositiveIntegerField(default=0)

    def __unicode__(self, *args, **kwargs):
        return self.question.question_text + " - " + self.choice_text
