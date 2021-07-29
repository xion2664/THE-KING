from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from django.utils import timezone
from .models import *
from account.models import User

# 홈 메서드
def home(request) :
    rank_total = User.objects.all().order_by('-total_score')
    return render(request, 'home.html', {"rank_total":rank_total})

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
        new_board.choice = request.POST['type']
        new_board.created_at = timezone.datetime.now() 
        new_board.image = request.FILES.get('image')
        new_board.body = request.POST['body']

        user_id = request.user.id
        user = User.objects.get(id = user_id)
        new_board.author = user
        new_board.save()

        # choice의 생리활동 종류별로 점수 추가

        # 큰거일 때
        if new_board.choice == 'big' :

            save_score = User.objects.get(id = user_id)
            save_score.big_score += 5
            save_score.total_score += 5
            save_score.save()
        
        # 작은거일 때
        if new_board.choice == 'small' :

            save_score = User.objects.get(id = user_id)
            save_score.small_score += 3
            save_score.total_score += 3
            save_score.save()

        # 방구일 때
        if new_board.choice == 'gas' :

            save_score = User.objects.get(id = user_id)
            save_score.gas_score += 1
            save_score.total_score += 1
            save_score.save()

        return redirect('history')
    else :
        # GET 방식일때 단순 페이지 이동
        return render(request, 'new.html')

# 글 삭제 메서드
def delete(request, id) :
    delete_board = Board.objects.get(id = id)
    delete_board.delete()
    return redirect('home')

# 통합 순위 메서드
def total_rank(request):
    total_rank = User.objects.all().order_by('-total_score')
    return render(request, 'total-rank.html', {"total_rank":total_rank})

# 대변 순위 메서드
def big_rank(request):
    big_rank = User.objects.all().order_by('-big_score')
    return render(request, 'big-rank.html', {"big_rank":big_rank})

# 소변 순위 메서드
def small_rank(request):
    small_rank = User.objects.all().order_by('-small_score')
    return render(request, 'small-rank.html', {"small_rank":small_rank})

# 방귀 순위 메서드
def gas_rank(request):
    gas_rank = User.objects.all().order_by('-gas_score')
    return render(request, 'gas-rank.html', {"gas_rank":gas_rank})