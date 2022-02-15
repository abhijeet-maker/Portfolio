from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from Bio.models import User
from django.http import HttpResponse
# Create your views here.
def index(request):
    data=User.objects.all()
    achievements=User.objects.values('achievements')
    achievements=list(achievements)
    #list(achievements)
    #print("achievements-----------",achievements.get(achievements="achievements"))
    print(achievements[0])
    #print("achievements***********",achievements.tolist())
    #for user in data:
    #    print(user.first_name,user.last_name,user.address)
    #args={'user':user}

    #data={'first_name':"Abhi",'last_name':"jeet",'address':"qwerty",'about':"wqertyuii"}
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    #return render(request, 'index.html',{'user':user})

    return render(request, 'index.html',{'data':data,'achievements':achievements})