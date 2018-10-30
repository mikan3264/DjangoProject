from django.contrib import admin

#ここにmodelクラスを登録することで管理サイトからDB編集が可能になる
from .models import Question
from .models import Choice
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
