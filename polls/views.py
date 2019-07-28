from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Questions

# Create your views here.
def index(request):
    # 1st index func contents
    # return HttpResponse("Hello world. This is my refresher poll app")
    # 2nd func contents
    # latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    # return  HttpResponse(output)
    # 3rd func contents
    # latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question_list' : latest_question_list,}
    # return HttpResponse(template.render(context,request))
    # 4th  func contents
    latest_question_list = Questions.objects.order_by('-pub_date').[:5]
    context = {'latest_question_list' : latest_question_list,}
    return render(request,'polls/index.html',context)
def detail(request, question_id):
    return HttpResponse("you are looking at question %s." %question_id)
def results(request, question_id):
    response = "You are looking at the results of Questions %s"
    return HttpResponse(response %question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on Question %s." %question_id)
def vote1(request, question_id):
    return HttpResponse("You are voting on Question %s." %question_id)