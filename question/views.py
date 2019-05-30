from django.shortcuts import render,get_object_or_404,redirect
from .forms import BoardForm
from .models import Board #, Like
from django.utils import timezone
# try:
#     from django.utils import simplejson as json
# except ImportError:
#     import json
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST
# Create your views here.

def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date =timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request,'post.html',{'form':form})    

def show(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'show.html', {'boards':boards})

def detail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request,'detail.html', {'board':board_detail})  
def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)  
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board) 
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm(instance=board)
        return render(request,'edit.html',{'form':form})

def delete(request,pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('show')
 

# @login_required
# @require_POST
# def like(request):
#     pk = request.Board.get('pk', None)
#     post = get_object_or_404(Board, pk=pk)
#     post_like, post_like_created = post.like_set.get_or_create(user=request.user)

#     if not post_like_created:
#         post_like.delete()
#         message = "좋아요 취소"
#     else:
#         message = "좋아요"

#     context = {'like_count': post.like_count,
#                'message': message,
#                'nickname': request.user.profile.nickname}

#     return HttpResponse(json.dumps(context), content_type="application/json")
