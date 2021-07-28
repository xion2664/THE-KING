from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.decorators import login_required

from .models import User
from board.models import Board
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

#회원 탈퇴
def user_delete(request) :
    if request.method == "POST" :
        password_del = request.POST["password_del"]
        user = request.user
        if check_password(password_del, user.password) :
            user.delete()
            return redirect('home')
    else :
        return render(request, 'delete.html')


# 랭킹 정렬
def rank(request) :
    rank_big = User.objects.all().order_by('big_score')
    rank_small = User.objects.all().order_by('small_score')
    rank_gas = User.objects.all().order_by('gas_score')
    rank_total = User.objects.all().order_by('total_score')
    return render(request, 'rank.html', {'rank_big': rank_big}, {'rank_small':rank_small}, {'rank_gas':rank_gas}, {'rank_total':rank_total})

# 마이페이지
def mypage(request) :
    #로그인 안된 사용자 접근 제한
    if request.method == 'GET':
        return render(request, 'mypage.html')

# 개인 정보 수정
def user_update(request, id) :
    if request.method == 'POST' :
        user_update = User.objects.get(id = id)
        user_update.nickname = request.POST["nickname"]
        user_update.profile = request.FILES.get('profile')
        user_update.save()
        return redirect('mypage')
    else :
        return render(request, 'update.html')



def history(request) :
    print("sakfdds", request.user)
    boards = Board.objects.all()
    board_list = boards.filter(author = request.user)
    return render(request, 'history.html', {'board_list' : board_list})
