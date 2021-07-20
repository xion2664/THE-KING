from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from django.contrib import auth

# Create your views here.

# 회원가입
def user_signup(request) :
    if request.method == 'POST' :
        if request.POST['password'] == request.POST["password2"] :
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],

                nickname = request.POST["nickname"],
                profile = request.FILES.get("profile")
            )
            user.save()
            auth.login(request, user)
            return redirect('home')

        else :
            return render(request, 'signup.html')
    else :
        return render(request, 'signup.html')

# 로그인
def user_login(request) :
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None :
            login(request, user)
            return redirect('home')

        else :
            return render(request, 'login.html', {'error':'아이디와 비밀번호가 일치하지 않습니다.'})
    
    else :
        return render(request, 'login.html')

# 로그아웃
def user_logout(request) :
    logout(request)
    return redirect('home')


# 랭킹 정렬
def rank(request) :
    rank_big = User.objects.all().order_by('big_score')
    rank_small = User.objects.all().order_by('small_score')
    rank_gas = User.objects.all().order_by('gas_score')
    rank_total = User.objects.all().order_by('total_score')
    return render(request, 'rank.html', {'rank_big': rank_big}, {'rank_small':rank_small}, {'rank_gas':rank_gas}, {'rank_total':rank_total})


# 마이페이지
def mypage(request) :
    return render(request, 'mypage.html')