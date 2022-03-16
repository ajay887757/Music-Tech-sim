from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from song.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint

def f1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = students.objects.all()
    data2=college.objects.all()
    a="pythobn dajango class"
    d={"Hello":data,"key2":data2}
    return render(request,"index1.html",d)
def f2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    d={"H":"Welcome to Jungle","E":"Ajay","A":"Piyush"}
    return render(request,"index2.html",d)
def f3(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data3 = friend.objects.all()
    d={"key3":data3}
    return render(request,"index3.html",d)
def Detail(request,s_id):
    if not request.user.is_authenticated:
        return redirect('login')
    data=students.objects.get(id=s_id)
    d={"stu":data}
    return render(request,"detail.html",d)

def operations(request):
    if not request.user.is_authenticated:
        return redirect('login')
    a=0
    o=0
    if request.method== "POST":
        V1 =request.POST['v1']
        V2 =request.POST['v2']
        o = request.POST['op']
        try:
            if o == 'Add':
                a=int(V1)+int(V2)
            elif o == 'Sub':
                a=int(V1)-int(V2)
            elif o == 'Mul':
                a = int(V1) * int(V2)
            elif o=='Div':
                a = int(V1) / int(V2)
            else:
                a=str(V1) +str(" ") + str(V2)
        except:
             return HttpResponse("wrong Input")
    d={
         "out":a,"output":o
     }
    return render(request,"operation.html",d)

def Add_student(request):
    allcollege=college.objects.all()
    dd={"allcollege":allcollege}
    if request.method=="POST":
        d=request.POST
        s= d['sname']
        m= d['mob']
        e= d['em']

        b= d['enroll']
        c=d['cid']
        cdata=college.objects.get(id=c)
        try:
            i = request.FILES['url1']

            students.objects.create(Name=s,Gmail=e,Enrollment=b,image=i,Number=m,clg=cdata)
        except:
            students.objects.create(Name=s, Gmail=e, Enrollment=b, Number=m, clg=cdata)
        return redirect('Ajay')
    return render(request,'add_s.html',dd)
def Delete_student(request,sid):
    data= students.objects.get(id =sid)
    data.delete()
    return redirect('Ajay')
def Add_college(request):
    if request.method == "POST":
        d = request.POST
        s = d['cname']
        m = d['cmob']
        e = d['Add']
        college.objects.create(Name=s,contact=m,Address=e)
        return redirect('Ajay')
    return render(request,'Add_college.html')
def edit_student(request,sid):
    data = students.objects.get(id=sid)
    allcollege=college.objects.all()
    if request.method=="POST":
        a=request.POST
        s= a['sname']
        m= a['mob']
        e= a['em']
        b= a['enroll']
        c=a['cid']
        data.Name=s
        data.Number=m
        data.Gmail=e

        data.Enrollment=b
        clgdata=college.objects.get(id = c)
        data.clg=clgdata
        data.save()
        try:
            i = request.FILES['url1']
            data.image = i
            data.sava()
        except:
            pass
        return redirect('Detail',sid)
    d={"detail":data,"allcollege":allcollege}
    return render(request,'edit_student.html',d)
def edit_college(request,sid):
    data = college.objects.get(id=sid)
    if request.method == "POST":
        a = request.POST
        s = a['cname']
        m = a['Add']
        e = a['cmob']
        data.Name = s
        data.Address = m
        data.contact = e
        data.save()
        return redirect('Ajay')
    d = {"detail":data}
    return render(request, 'edit_college.html', d)
def delete_college(request,sid):
    data=college.objects.get(id=sid)
    data.delete()
    return redirect('Ajay')

def LoginForm(request):
    error=False
    if request.method=="POST":
        d=request.POST
        u=d['user']
        p=d['pwd']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('Ajay')
        else:
            error=True
    d={"error":error}
    return render(request,'login.html',d)
def Logout(request):
    logout(request)
    return redirect('login')
def signup(request):
    error=False
    error2=False
    if request.method=="POST":
        d=request.POST
        u=d['user']
        p=d['pwd']
        c=d['cpwd']
        f=d['f_name']
        l=d['l_name']
        e=d['email']
        user=User.objects.filter(username=u)
        if user:
            error2=True
        elif c!=p:
            error=True
        else:
            User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            return redirect('login')
    dd={"error":error,"error2":error2}
    return render(request,'signup.html',dd)
#def Add_univercity(request):
   # if request.method == "POST":
      # d = request.POST
       # s = d['uname']
       # m = d['umob']
       # e = d['Add']
        #college.objects.create(Name=s,contact=m,Address=e)
        #return redirect('Ajay')
   # return render(request,'Add_college.html')
def forget(request):
    form=False
    error=False
    udata=False
    if request.method=="POST":
        dd=request.POST
        name=dd['form']
        if name=="submit email":
            e = dd['em']
            user=User.objects.filter(email = e)
            if user:
                form =True
                udata=user[0]
            else:
                error=True
        if name =='submit pwd':
                print("Hello........")
                p=dd['pwd']
                cp=dd['cpwd']
                u=dd['idd']
                user=User.objects.get(id=u)
                user.set_password(p)
                user.save()
                return redirect('login')
    d={"form":form,"error":error,"udata":udata}
    return render(request,'forget.html',d)







