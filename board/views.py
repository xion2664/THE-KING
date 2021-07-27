from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from django.utils import timezone
from .models import *

# 홈 메서드
def home(request) :
    return render(request, 'home.html')

# 글 디테일 메서드
def detail(request, id) :
    board = get_object_or_404(Board, pk = id)
    return render(request, 'detail.html', {'board':board})

# 글 수정 메서드
def edit(request, id) :
    if request.method == "POST":
        # POST 방식일떄 기존 글 수정
        edit_board = Board.objects.get(id = id)
        edit_board.choice = request.POST['choice']
        edit_board.created_at= timezone.datetime.now()
        edit_board.image = request.FILES.get('image')
        edit_board.body = request.POST['body']
        edit_board.save()
        return redirect('detail', edit_board.id)
    else :
        # GET 방식일때 단순 페이지 이동
        board = Board.objects.get(id = id)
        return render(request, 'edit.html', {'board': board})

# 글 업로드 메서드
def upload(request) :
    if request.method == "POST":
        # POST 방식일떄 새로운 글 생성
        new_board = Board()
        new_board.choice= request.POST.get('choice')
        new_board.created_at = timezone.datetime.now() 
        new_board.image = request.FILES.get('image') 
        new_board.body = request.POST.get('body')
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        new_board.author = user
        new_board.save() 
 
        return redirect('home')
    else :
        # GET 방식일때 단순 페이지 이동
        return render(request, 'new.html')

# 글 삭제 메서드
def delete(request, id) :
    delete_board = Board.objects.get(id = id)
    delete_board.delete()
    return redirect('home')
