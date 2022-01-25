from django.shortcuts import render, redirect


# Create your views here.
def login(request):


    context = {

    }

    return render(request, 'sign/login.html', context)

def login2(request):
    print("login2 호출 됨")
    data = request.POST
    print(data.get('inputEmail'))
    print(data.get('inputPassword'))
    



    return redirect('/main')

def register(request):

    context = {

    }

    return render(request, 'sign/register.html', context)