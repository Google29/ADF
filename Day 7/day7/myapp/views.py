from django.shortcuts import render
from django.http import  HttpResponse
from .form import Front
from .models import Newapp
from django.core.exceptions import ValidationError
import datetime
def create(request):
    if(request.method=="POST"):
        one = request.POST['first_name']
        two = request.POST['middle_name']
        three = request.POST['last_name']
        four = request.POST['dob']
        five = request.POST['gender']
        six = request.POST['nationality']
        seven = request.POST['city']
        eight = request.POST['state']
        nine = request.POST['pin_code']
        ten = request.POST['qualification']
        eleven = request.POST['salary']
        twelve = request.POST['pan']
        ins=Newapp(first_name=one, middle_name=two, last_name=three, DOB=four, gender=five, nationality=six
                        ,city=seven, state=eight, pin_code=nine, qualification=ten, salary=eleven, PAN=twelve)
        try:
            ins.save()
        except ValidationError:
            return HttpResponse('<h2>Invalid data entered<h2>')
        value=Newapp.objects.last()
        age=int(int((datetime.date.today()-value.DOB).days)/365)
        if (age<22 and value.gender=='male') or (age<19 and value.gender=='female' ) or age>100:
            return HttpResponse('<h2>Rejected:Age is lesser than expected<h2>')
        if value.nationality=='Others':
            return HttpResponse('<h2>Rejected:Nationality is not eligible<h2>')
        if int(value.salary)<10000 or int(value.salary)>90000:
            return HttpResponse('<h2>Rejected:Salary is out of range for eligibility<h2>')
        return HttpResponse('<h2>Success<h2>')
def level(request):
    context={
        "form" : Front(),
    }
    return render(request,'myapp/index.html',context)
