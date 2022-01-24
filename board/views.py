from django.shortcuts import render

# Create your views here.
from board.models import Board


def boardList(request):
    print('boardList 호출')

    board_list = Board.objects.order_by('-id')
    print('db_Board_List >> ', board_list)

    context = {
        'list': board_list
    }

    return render(request, 'board/boardList.html', context)