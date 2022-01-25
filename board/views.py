from django.shortcuts import render

# Create your views here.
from board.models import Board


def boardList(request):
    print('boardList 호출')

    qs = Board.objects.order_by('-id')
    print('db_Board_List >> ', qs)
    board_list = qs.values()

    context = {
        'list': board_list
    }

    return render(request, 'board/boardList.html', context)

def insert(request):
    print('insert 호출')
    data = request.POST

    print('content >> ', data.get('content'))
    print('writer >> ', data.get('writer'))

    context = {
        "list": data,
    }



    return render(request, 'board/boardList.html', context)