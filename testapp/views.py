from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")        #テスト出力
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
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
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
