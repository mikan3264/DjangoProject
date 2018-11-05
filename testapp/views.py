from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")        #テスト出力
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]       #Questionオブジェクトの最新5件を表示
    #output = ', '.join([q.question_text for q in latest_question_list])    #出力リスト作成。デバッグに使えそう
    template = loader.get_template('testapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(output)                                            #作成した出力リストをHttpResponseに詰めて返す。デバッグでとりあえず出力する際に使えそう
    #return HttpResponse(template.render(context, request))                 #HttpResponseにtemplateを詰めて返すやり方
    return render(request, 'testapp/index.html', context)                   #renderでtemplateを直接指定。これが一番シンプル

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)    #テスト出力
#def detail(request, question_id):                                          #オブジェクトをgetし存在しなければ404エラー。しかしコードが冗長である
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'testapp/detail.html', {'question': question})
def detail(request, question_id):                                           #get_object_or_404のショートカットを使ってオブジェクト取得と404エラー判定を同時に行う
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'testapp/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'testapp/results.html', {'question': question})

#---------------------------------------------------------------------------------------------------------------------------------------
# 以上は簡単だが冗長な書き方。以下は汎用ビューを使った書き方
class IndexView(generic.ListView):
    template_name = 'testapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'testapp/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'testapp/results.html'

def vote(request, question_id):
    # Questionオブジェクトを取得
    question = get_object_or_404(Question, pk=question_id)
    try:
        # formで渡されたchoice_idからchoiceオブジェクトを取得
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # postメソッドにchoiceが存在しなければエラー
        return render(request, 'testapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # オブジェクト取得に成功していれば投票数を加算し、DB保存。
        #selected_choice.votes += 1
        # F()でDBアクセスの競合を防いでくれるらしい。see also"https://docs.djangoproject.com/ja/2.1/ref/models/expressions/#avoiding-race-conditions-using-f"
        # "https://qiita.com/okoppe8/items/66a8747cf179a538355b"
        selected_choice.votes = F('votes') + 1;
        selected_choice.save()
        
        # 結果ページへリダイレクト
        return HttpResponseRedirect(reverse('testapp:results', args=(question.id,)))

# Create your views here.
