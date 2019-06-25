from django.shortcuts import render
from django.http import  HttpResponse
from .models import Questions

# Create your views here.
def index(request):
    # intial index func contents
    # return HttpResponse("Hello world. This is my refresher poll app")
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return  HttpResponse(output)
def detail(request, question_id):
    return HttpResponse("you are looking at question %s." %question_id)
def results(request, question_id):
    response = "You are looking at the results of Questions %s"
    return HttpResponse(response %question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on Question %s." %question_id)
