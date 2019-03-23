from django.db import models

# Create your models here.
# ○○Fieldとなっているものは、Filedインスタンスである

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published') # 人間に可読可能な名前を付けた

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Choiceが1つのQuestionに対応していると定義している
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)