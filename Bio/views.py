from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from Bio.models import User
from django.http import HttpResponse
# Create your views here.
def admin(request):
    return render(request, 'admin.html')

def index(request):
    data=User.objects.all()
    achievements=User.objects.values('achievements')
    achievements=list(achievements)
    print("achievements", achievements, "**********")
    if len(achievements) !=0:
        achievements=str(achievements[0]).split(":")[1]
        achievements=achievements.split("'")[1]
        achievements=achievements.split("\\r\\n")
    else:
        pass
    job_description=User.objects.values('job_description')
    job_descriptions=list(job_description)
    if len(job_descriptions) != 0:
        job_descriptions = str(job_descriptions[0]).split(":")[1]
        #print(job_descriptions)
        job_descriptions = job_descriptions.split("'")[1]
        job_descriptions = job_descriptions.split("\\r\\n\\r\\n")
    else:
        pass
    print("job_description", job_descriptions)
    #achievements=list(achievements)
    #achievements=achievements
    #print("achievements-----------",achievements.get(achievements="achievements"))
    print("achievements",achievements,"**********")
    #print("achievements**********", list(achievements[0]))
    #print("achievements*****",str(achievements[0]))
    #print("achievements*****",str(achievements[0]).split(":")[1])
    #print("achievements***********",achievements.tolist())
    #for user in data:
    #    print(user.first_name,user.last_name,user.address)
    #args={'user':user}

    #data={'first_name':"Abhi",'last_name':"jeet",'address':"qwerty",'about':"wqertyuii"}
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    #return render(request, 'index.html',{'user':user})

    return render(request, 'index.html',{'data':data,'achievements':achievements,'job_descriptions':job_descriptions})