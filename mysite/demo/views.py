from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import userForm,myform,user1form, StudentForm,carForm
from .models import cake

# Create your views here.
def main(request):
    # return HttpResponse('hello')
    data={
        'title':'demo',
        'main':'hiii',
        'subject':['maths','social'],
        'digit':[],
        'detail':[
            {'name':'abc','ph_no':4562389},
            {'name':'abcd','ph_no':565798}
        ]
    }
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")
def rooms(request):
    return render(request,"rooms.html")
def about(request):
    fname=request.GET['fname']
    lname=request.GET['lname']
    email=request.GET.get('email')
    password=request.GET['password']
    date=request.GET['date']
    number=request.GET['number']

    text={
        'n1':fname,
        'n2':lname,
        'n6':email,
        'n3':password,
        'n4':date,
        'n5':number,
       
    }
    print(text)
    return render(request,"about.html",text)
def contact(request):
    text={}
    try:
        fname=request.POST['First name']
        lname=request.POST['Last name']
        email=request.POST['Email']
        password=request.POST['Password']
        date=request.POST['Date']
        number=request.POST['Number']
        
        text={
        'fname':fname,
        'lname':lname,
        'email':email,
        'password':password,
        'date':date,
        'number':number,
        }

        # print(fname, number)
        url = f'/about/?fname={fname}&lname={lname}&email={email}&password={password}&date={date}&number={number}'
        return HttpResponseRedirect(url)

    except:
        pass
    return render(request,"contact.html", text)
def demo(request):
    # form=myform()
    if request.POST:
        form=StudentForm(request.POST) 
        if form.is_valid:
            form.save()
    form = StudentForm()
    

    return render(request, 'demo.html',{'form':form})

def result(request):
    firstname=int(request.POST['Fname'])
    lastname=int(request.POST['Lname'])
    email=int(request.POST['Email'])
    password=int(request.POST['Password'])
    phonenumber=int(request.POST['Phonenumber'])
   
    context={
       'Fname':firstname,
       'Lname':lastname,
       'Email':email,
       'Password':password,
       'Phonenumber':phonenumber,
    }

    return render(request, 'result.html', context)
def demo1(request):
    form=userForm()

    return render(request,'demo1.html',{'form':form})
def result1(request):
    valu1=int(request.POST['Value1'])
    valu2=int(request.POST['Value2'])
    context={
        'value1':valu1,
        'value2':valu2,
        'avg':(valu1+valu2)/2,
    }
    return render(request, 'result1.html', context)


def d(request):
    form=user1form()
    return render(request,'d.html',{'form':form})
def r(request):
    num1=int(request.POST['n1'])
    num2=int(request.POST['n2'])
    t=request.POST['operator']
    # result=request.POST['result']
    # text={'+':num1+num2,'-':num1-num2,'*':num1*num2,'/':num1/num2}
    # for keys,values in text.items():
    #     if t==keys:
    #         result=values

    if t=="+":
        result=num1+num2
    elif t=='-':
        result=num1-num2
    elif t=='*':
        result=num1*num2
    elif t=='/':
        result=num1/num2
    context={
        'n1':num1,
        'n2':num2, 
        'operator':t,
        'result':result
    }
    return render(request,'r.html',context)

def cakess(request):
    cakes=cake.objects.all().order_by('-title')
    data={
        'rec':cakes
    }
    return render(request,'cake.html',data)


def detail(request, id):
    cak=cake.objects.get(id=id)
    return render(request,'result.html',{'cake':cak})

def car(request):
    if request.POST:
        form=carForm(request.POST) 
        if form.is_valid:
            form.save()
    form=carForm()
    return render(request,'car.html',{'form':form})

def maclloc(request):
    return render(request,'maclloc.html')