from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login, logout

 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return redirect('main:index')
        else:
            print("인증실패")    
    return render(request, "login.html")
        

def signup(request):
    if request.method == "POST": # 요청메시지가 post 라면
        print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2 :
            return HttpResponse('비밀번호가 다릅니다.')
        fullname = request.POST.get("fullname")
        age = request.POST.get("age")
        gender = request.POST.get('gender')
        phone = request.POST.get("phone")
        parmacy = request.POST.get("parmacy")
        relation = request.POST.get("relation")
        

        user = User.objects.create_user(username, email, password)
        user.fullname = fullname
        user.password2 = password2
        user.age = age
        user.gender = gender
        user.phone = phone
        user.parmacy = parmacy
        user.relation = relation
        user.save()

        
        return redirect("member:login")

    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect("member:login")
