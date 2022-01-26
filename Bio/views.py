from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from Bio.models import User
from django.http import HttpResponse
# Create your views here.
def index(request):
    user=User.objects.get()

    #user={'first_name':"Abhi",'last_name':"jeet"}
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    #return render(request, 'index.html',{'user':user})
    return render(request, 'index.html',{'user':user})