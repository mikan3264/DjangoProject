from django.contrib import admin

#ここにmodelクラスを登録することで管理サイトからDB編集が可能になる
from .models import Question
from .models import Choice

# このクラスをQuestionAdminのinlinesに登録することでQuestion側から選択肢の追加が可能になる
#class ChoiceInline(admin.StackedInline):   #これは一般的な形のリストで表示
class ChoiceInline(admin.TabularInline):    #これはコンパクトなテーブル形式で表示
    model = Choice
    extra = 1

# このような記述のクラスを作り登録処理に渡すと入力フィールドの表示順序を変えられる。
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

# 以下は入力フィールドをカテゴリごとに分けるやり方
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # Question一覧の画面でstr()の値だけでなく他の情報も表示する。
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # boolの値をソートに利用する場合に必要？modelsのQuestionsにも追記あり。
    list_filter = ['pub_date']

    # 検索窓追加。入力文字列とquestion_textを比較して検索する。
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
