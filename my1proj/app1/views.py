from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from app1.models import Contestants

def phone_format(phone):

    ...

def indexpage(request):
    if request.method == 'POST':
        name = request.POST['fio']
        stud = request.POST['stud']
        phone = request.POST['phone']
        email = request.POST['email']
        print(name, stud, phone, email)
        sname = name.split(' ')
        l_name, f_name, m_name = sname[0], sname[1], sname[2]

        contest = Contestants(lastname=l_name, firstname=f_name, midname=m_name,institution=stud, phone_number=phone, email=email)
        contest.save()

    return render(request, 'index.html')
